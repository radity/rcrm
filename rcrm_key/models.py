from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from rcrm_core.models import DateModel


class UniqueKey(DateModel):
    # Base
    key = models.CharField(verbose_name=_('Key'), max_length=50, unique=True)
    is_used = models.BooleanField(verbose_name=_('Used'), default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return '{key}'.format(key=self.key)


class ResetPasswordKey(UniqueKey):
    # Relations
    user = models.ForeignKey(
        verbose_name=_('User'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reset_password_keys'
    )

    class Meta:
        verbose_name = _('Reset Password Key')
        verbose_name_plural = _('Reset Password Keys')

    def __str__(self):
        return '{key}'.format(key=self.key)
