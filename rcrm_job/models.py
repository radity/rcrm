from django.db.models import Model, CASCADE, \
    BooleanField, CharField, DateTimeField,\
    ForeignKey, TextField, URLField
from django.utils.translation import ugettext_lazy as _

from rcrm_account.models import CRMAccount
from rcrm_contact.utils import COUNTRIES

# Create your models here.


class Job(Model):
    account = ForeignKey(CRMAccount, on_delete=CASCADE)
    title = CharField(max_length=256)
    description = TextField(max_length=1024)
    url = URLField(_('URL'), max_length=2048, null=True, blank=True)
    office = CharField(max_length=128)
    city = CharField(max_length=128)
    country = CharField(max_length=2, choices=COUNTRIES)

    # Status
    is_active = BooleanField(_('Is Active?'), default=True)
    is_deleted = BooleanField(_('Is Deleted?'), default=False)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('account__name', 'title')
        verbose_name = _('Job Opportunity')
        verbose_name_plural = _('Job Opportunities')

    def __str__(self):
        return self.title

