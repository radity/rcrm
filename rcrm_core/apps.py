from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class RcrmCoreConfig(AppConfig):
    name = 'rcrm_core'
    verbose_name = _('Core')
