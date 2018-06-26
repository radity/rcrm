from django.db.models import Model, \
    BooleanField, CharField, DateTimeField, \
    EmailField, ManyToManyField, TextField
from django.utils.translation import ugettext_lazy as _

from rcrm_contact.models import Contact
from rcrm_utils.models import Email, Phone


# Create your models here.


class Account(Model):
    contact = ManyToManyField(Contact)
    name = CharField(_('Account Name'), max_length=64)
    phone = ManyToManyField(Phone)
    email = ManyToManyField(Email)
    description = TextField(_('Short Description'), max_length=256, null=True, blank=True)

    # Status
    is_active = BooleanField(_('Is Active?'), default=True)
    is_deleted = BooleanField(_('Is Deleted?'), default=False)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    def __str__(self):
        return self.name

    def get_phones(self):
        return "\n-\n".join([p.phone for p in self.phone.all()[:2]])
    get_phones.short_description = "Phone"

    def get_emails(self):
        return "\n-\n".join([p.email for p in self.email.all()[:2]])
    get_emails.short_description = "Email"
