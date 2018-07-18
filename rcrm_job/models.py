from django.db.models import Model, CASCADE, \
    BooleanField, CharField, DateTimeField,\
    ForeignKey, TextField, URLField,\
    ImageField
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import reverse

from rcrm_account.models import CRMAccount
from rcrm_contact.utils import COUNTRIES
from rcrm_job.utils import TYPE_OF_EMPLOYMENT

from ckeditor.fields import RichTextField

# Create your models here.


class Job(Model):
    account = ForeignKey(CRMAccount, on_delete=CASCADE)
    title = CharField(max_length=128)
    short_description = TextField(max_length=256)
    description = RichTextField(max_length=4096)
    type_of_employment = CharField(max_length=1, choices=TYPE_OF_EMPLOYMENT)

    # Requirements
    talent = CharField(max_length=512)
    experience = CharField(max_length=8)
    education_level = CharField(max_length=32)
    language = CharField(max_length=64)

    # Location
    office = CharField(max_length=128)
    city = CharField(max_length=128)
    country = CharField(max_length=2, choices=COUNTRIES)

    # Extra
    url = URLField(_('URL'), max_length=2048, null=True, blank=True)
    image = ImageField(upload_to='job/', null=True, blank=True)

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

    def get_absolute_url(self):
        return reverse('Jobs:Job_Detail', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('Jobs:Job_Edit', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('Jobs:Job_Delete', kwargs={'pk': self.id})