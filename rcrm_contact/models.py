from django.db.models import Model, CASCADE, \
    BooleanField, CharField, DateField, \
    EmailField, DateTimeField, ForeignKey, \
    TextField, URLField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from rcrm_account.models import CRMAccount
from rcrm_contact.utils import COUNTRIES, GENDER

from location_field.models.plain import PlainLocationField


# Create your models here.


class Contact(Model):
    """
    This model is like a person who is imagined as a customer.
    """
    account = ForeignKey(CRMAccount, on_delete=CASCADE)
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)
    gender = CharField(max_length=1, choices=GENDER)
    title = CharField(_('Position/Title'), max_length=32, null=True, blank=True)
    date_of_birth = DateField(_('Date of Birth'), null=True, blank=True)
    description = TextField(_('Short Description'), max_length=256, null=True, blank=True)

    # Status
    is_active = BooleanField(_('Is Active?'), default=True)
    is_deleted = BooleanField(_('Is Deleted?'), default=False)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def addresses(self):
        return Address.objects.filter(contact=self)

    def emails(self):
        return Email.objects.filter(contact=self)

    def phones(self):
        return Phone.objects.filter(contact=self)

    def social_profiles(self):
        return SocialProfile.objects.filter(contact=self)

    def get_absolute_url(self):
        return reverse('Contacts:Contact_Detail', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('Contacts:Contact_Edit', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('Contacts:Contact_Delete', kwargs={'pk': self.id})

    def get_add_phone_url(self):
        return reverse('Contacts:Phone_Create', kwargs={'pk': self.id})

    def get_add_email_url(self):
        return reverse('Contacts:Email_Create', kwargs={'pk': self.id})

    def get_add_address_url(self):
        return reverse('Contacts:Address_Create', kwargs={'pk': self.id})

    def get_add_social_url(self):
        return reverse('Contacts:Social_Create', kwargs={'pk': self.id})

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    get_full_name.short_description = "Full Name"

    def save(self, **kwargs):
        self.account = self.account or self.contact_account()
        super(Contact, self).save(**kwargs)

    def contact_account(self):
        account = self.request.user.account
        return account


class Address(Model):
    """
    Contact's Address
    """
    contact = ForeignKey(Contact, on_delete=CASCADE, related_name='Contact_Address')
    title = CharField(_('Address Title'), max_length=64, help_text="Radity Headquarter Zurich")
    address = CharField(_("Address"), max_length=255, blank=True, null=True)
    map = PlainLocationField(based_fields=['address'], zoom=7)
    city = CharField(_("City"), max_length=255, blank=True, null=True)
    state = CharField(_("State"), max_length=255, blank=True, null=True)
    postcode = CharField(_("Post/Zip-code"), max_length=64, blank=True, null=True)
    country = CharField(max_length=2, choices=COUNTRIES, blank=True, null=True)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    def __str__(self):
        return self.title

    @property
    def full_address(self):
        full_address = '%s, %s, %s, %s, %s' % (self.address, self.state, self.city, self.postcode, self.country)
        return full_address

    def get_edit_url(self):
        return reverse('Contacts:Address_Edit', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('Contacts:Address_Delete', kwargs={'pk': self.id})

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class SocialProfile(Model):
    """
    Contact's Social Profile
    """
    contact = ForeignKey(Contact, on_delete=CASCADE, related_name='Contact_Social_Profile')
    title = CharField(_('Social Profile Title'), max_length=64, help_text="Ex: Mr. Ozgur Aksakal's Social Profile")
    website = URLField(_('Website'), max_length=128, null=True, blank=True)
    linkedin = URLField(_('Linkedin URL'), max_length=2048, null=True, blank=True)
    skype = CharField(_('Skype'), max_length=128, help_text="@username", null=True, blank=True)
    facebook = URLField(_('Facebook URL'), max_length=2048, null=True, blank=True)
    twitter = CharField(_('Twitter'), max_length=128, help_text="@username", null=True, blank=True)
    instagram = CharField(_('Instagram'), max_length=128, help_text="@username", null=True, blank=True)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    def __str__(self):
        return self.title

    def get_edit_url(self):
        return reverse('Contacts:Social_Edit', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('Contacts:Social_Delete', kwargs={'pk': self.id})

    class Meta:
        verbose_name = _('Social Profile')
        verbose_name_plural = _('Social Profiles')


class Phone(Model):
    """
    Contact's Phone.
    """
    contact = ForeignKey(Contact, on_delete=CASCADE, related_name='Contact_Phone')
    title = CharField(_('Phone Title'), max_length=32, help_text="Ex: Mr. Ozgur Aksakal's Phone Number")
    phone = CharField(max_length=16)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    def __str__(self):
        return self.title

    def get_edit_url(self):
        return reverse('Contacts:Phone_Edit', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('Contacts:Phone_Delete', kwargs={'pk': self.id})


class Email(Model):
    """
    Contact's Email
    """
    contact = ForeignKey(Contact, on_delete=CASCADE, related_name='Contact_Email')
    title = CharField(_('Email Title'), max_length=32, help_text="Ex: Mr. Ozgur Aksakal's Email Address")
    email = EmailField(max_length=64)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    def __str__(self):
        return self.title

    def get_edit_url(self):
        return reverse('Contacts:Email_Edit', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('Contacts:Email_Delete', kwargs={'pk': self.id})
