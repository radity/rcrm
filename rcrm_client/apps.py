from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class RcrmClientConfig(AppConfig):
    name = 'rcrm_client'
    verbose_name = _('Clients')