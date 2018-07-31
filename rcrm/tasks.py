# Django
from django.conf import settings
from django.utils import translation
from django.core.mail import send_mail

# Local Django
from rcrm import celery_app


@celery_app.task
def mail_task(context, verb):
    """
    Context Format
        context = {
            subject="subject"
            message="messages"
            html_message=render_to_string('email/email.html', template_context),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email]
        }
    """

    message = ''

    try:
        send_mail(**context)

        message = '{recipient_list} success. ({verb})'.format(
            recipient_list=','.join(context['recipient_list']), verb=verb
        )
    except Exception as err:
        message = '{recipient_list} error. ({verb}) - ({err})'.format(
            recipient_list=','.join(context['recipient_list']), verb=verb, err=err
        )

    return message
