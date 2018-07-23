from django.db.models import Model, CASCADE, \
    BooleanField, CharField, DateField, \
    EmailField, DateTimeField, ForeignKey, \
    TextField, URLField, ImageField,\
    FileField, ManyToManyField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from rcrm_account.models import CRMAccount
from rcrm_contact.models import Contact
from rcrm_util.models import Address, Email, Phone, SocialProfile


# Create your models here.


class Client(Model):
    """
    Customer Client.
    """
    account = ForeignKey(CRMAccount, on_delete=CASCADE)
    name = CharField(max_length=128)
    description = TextField(null=True, blank=True)

    # Contact Persons
    contact = ManyToManyField(Contact, blank=True)

    # Contact
    phone = ManyToManyField(Phone, blank=True)
    address = ManyToManyField(Address, blank=True)
    email = ManyToManyField(Email, blank=True)
    social = ManyToManyField(SocialProfile, blank=True)

    # Status
    is_active = BooleanField(_('Is Active?'), default=True)
    is_deleted = BooleanField(_('Is Deleted?'), default=False)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_phones(self):
        return "\n-\n".join([p.phone for p in self.phone.all()[:2]])
    get_phones.short_description = "Phone"

    def get_emails(self):
        return "\n-\n".join([p.email for p in self.email.all()[:2]])
    get_emails.short_description = "Email"

    def get_absolute_url(self):
        return reverse('Clients:Client_Detail', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('Clients:Client_Edit', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('Clients:Client_Delete', kwargs={'pk': self.id})

    def get_contact_create_url(self):
        return reverse('Clients:Contact_Create', kwargs={'pk': self.id})

    def get_add_contact_url(self):
        return reverse('Clients:Contact_Add', kwargs={'pk': self.id})

    def get_contact_delete_url(self):
        return reverse('Clients:Contact_Delete', kwargs={'pk': self.id})

    def get_add_phone_url(self):
        return reverse('Clients:Phone_Create', kwargs={'pk': self.id})

    def get_edit_phone_url(self):
        return reverse('Clients:Phone_Edit', kwargs={'client_id': self.id})

    def get_delete_phone_url(self):
        return reverse('Clients:Phone_Delete', kwargs={'client_id': self.id})

    def get_add_email_url(self):
        return reverse('Clients:Email_Create', kwargs={'pk': self.id})

    def get_edit_email_url(self):
        return reverse('Clients:Email_Edit', kwargs={'client_id': self.id})

    def get_delete_email_url(self):
        return reverse('Clients:Email_Delete', kwargs={'client_id': self.id})

    def get_add_address_url(self):
        return reverse('Clients:Address_Create', kwargs={'pk': self.id})

    def get_edit_address_url(self):
        return reverse('Clients:Address_Edit', kwargs={'client_id': self.id})

    def get_delete_address_url(self):
        return reverse('Clients:Address_Delete', kwargs={'client_id': self.id})

    def get_add_social_url(self):
        return reverse('Clients:Social_Create', kwargs={'pk': self.id})

    def get_edit_social_url(self):
        return reverse('Clients:Social_Edit', kwargs={'client_id': self.id})

    def get_delete_social_url(self):
        return reverse('Clients:Social_Delete', kwargs={'client_id': self.id})
