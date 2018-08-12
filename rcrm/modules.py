from django.urls import reverse
from django.conf import settings
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from rcrm.tasks import mail_task
from rcrm_key.models import ResetPasswordKey
from rcrm.variables import KEY_MAX_LENGTH, UNIQUE_KEY_MODELS


class KeyModule(object):

    @staticmethod
    def uniqueness_check_key(key):
        model = None
        model_list = UNIQUE_KEY_MODELS

        for model_dict in model_list:
            try:
                model = ContentType.objects.get(
                    app_label=model_dict.get('app_label', ''), model=model_dict.get('model', '')
                )
            except ContentType.DoesNotExist:
                model = None
            except KeyError:
                model = None

            if model:
                instances = model.get_all_objects_for_this_type(key=key)

                if instances:
                    return False

        return True

    @staticmethod
    def create_unique_key(length=KEY_MAX_LENGTH):
        key = ''
        unique_key = False

        while unique_key==False:
            key = get_random_string(length=length)

            if KeyModule.uniqueness_check_key(key):
                unique_key  = True

        return key

    @staticmethod
    def create_reset_password_key(user):
        reset_password_key = None
        reset_password_keys = ResetPasswordKey.objects.filter(user=user, is_used=False)

        if not reset_password_keys:
            key = KeyModule.create_unique_key(length=KEY_MAX_LENGTH)
            reset_password_key = ResetPasswordKey(key=key, user=user)
            reset_password_key.save()
        else:
            reset_password_key = reset_password_keys.first()

        return reset_password_key

    @staticmethod
    def get_reset_password_key(key):
        try:
            reset_password_key = ResetPasswordKey.objects.get(key=key, is_used=False)
        except:
            reset_password_key = None

        return reset_password_key


class MailModule(object):

    @staticmethod
    def send_forgot_password_mail(user, request):
        reset_password_key = KeyModule.create_reset_password_key(user)
        reset_password_url = request.build_absolute_uri(
            reverse('Accounts:Reset_Password', args=[reset_password_key.key])
        )
        message = _(
            "RCRM \n"
            "Hello, {email} \n"
            "Reset Password = {reset_password_url}"
        ).format(email=user.email, reset_password_url=reset_password_url)

        context = {
            'subject': _('Forgot Password'),
            'message': message,
            #'html_message': message,
            'from_email': settings.DEFAULT_FROM_EMAIL,
            'recipient_list': [user.email],
            'fail_silently': False
        }

        mail_task.delay(context, 'forgot-password')

    def send_account_request_create_mail(account_users, user, request):
        url = request.build_absolute_uri(reverse('Accounts:Account'))
        message = _(
            '{user_email} requested to be a user of your account to '
            'accept/decline keep going on the link below.\n{url}'
        ).format(user_email=user.email, url=url)
        recipient_list = [account_user.email for account_user in account_users]

        context = {
            'subject': _('There is an Access Request to Your RCRM Account!'),
            'message': message,
            #'html_message': message,
            'from_email': settings.DEFAULT_FROM_EMAIL,
            'recipient_list': recipient_list,
            'fail_silently': False
        }
        mail_task.delay(context, 'account-request-create')

    def send_account_request_accept_mail(user, request):
        url = request.build_absolute_uri(reverse('Accounts:Account'))
        message = _(
            'Your RCRM account request has been accepted.\n'
            'To reach the account: {url}'
        ).format(url=url)

        context = {
            'subject': _('Your Request Has Been Accepted'),
            'message': message,
            #'html_message': message,
            'from_email': settings.DEFAULT_FROM_EMAIL,
            'recipient_list': [user.email],
            'fail_silently': False
        }

        mail_task.delay(context, 'account-request-accept')
