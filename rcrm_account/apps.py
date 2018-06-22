from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class RcrmAccountConfig(AppConfig):
    name = 'rcrm_account'
    verbose_name = "Account"


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'