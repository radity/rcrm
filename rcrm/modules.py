# Django
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from rcrm.variables import KEY_MAX_LENGTH, UNIQUE_KEY_MODELS
from rcrm_key.models import ResetPasswordKey


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
