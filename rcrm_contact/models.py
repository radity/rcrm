from django.db.models import Model, PROTECT, \
    BooleanField, CharField, DateField,\
    DateTimeField, EmailField, ForeignKey,\
    ManyToManyField, TextField
from django.utils.translation import ugettext_lazy as _

from rcrm_utils.models import Address, Email, SocialProfile, Phone
from rcrm_utils.utils import GENDER


# Create your models here.


class Contact(Model):
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)
    gender = CharField(max_length=1, choices=GENDER)
    title = CharField(_('Position/Title'), max_length=32, null=True, blank=True)
    date_of_birth = DateField(_('Date of Birth'), null=True, blank=True)
    description = TextField(_('Short Description'), max_length=256, null=True, blank=True)

    # Contact
    email = ManyToManyField(Email)
    phone = ManyToManyField(Phone)
    address = ManyToManyField(Address)

    # Status
    is_active = BooleanField(_('Is Active?'), default=True)
    is_deleted = BooleanField(_('Is Deleted?'), default=False)

    # Social
    social = ForeignKey(SocialProfile, on_delete=PROTECT, null=True, blank=True)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    def __str__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    get_full_name.short_description = "Full Name"

    def get_phones(self):
        return "\n-\n".join([p.phone for p in self.phone.all()])
    get_phones.short_description = "Phone"

    def get_emails(self):
        return "\n-\n".join([p.email for p in self.email.all()])
    get_emails.short_description = "Email"

