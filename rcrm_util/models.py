from django.db.models import Model, CASCADE, \
    BooleanField, CharField, DateField, \
    EmailField, DateTimeField, ForeignKey, \
    TextField, URLField, ImageField, FileField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from rcrm_util.utils import COUNTRIES


# Create your models here.

class Address(Model):
    title = CharField(_('Address Title'), max_length=64)
    address = CharField(_("Address"), max_length=255)
    city = CharField(_("City"), max_length=255)
    state = CharField(_("State"), max_length=255)
    postcode = CharField(_("Postcode"), max_length=64)
    country = CharField(_('Country'), max_length=2, choices=COUNTRIES, blank=True, null=True)

    # Status
    is_active = BooleanField(_('Is Active?'), default=True)
    is_deleted = BooleanField(_('Is Deleted?'), default=False)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __str__(self):
        return self.title

    @property
    def get_full_address(self):
        full_address = '%s, %s, %s, %s, %s' % (self.address, self.state, self.city, self.postcode, self.country)
        return full_address

    def get_edit_client_url(self):
        return reverse('Clients:Address_Edit', kwargs={'pk': self.id})

    def get_delete_client_url(self):
        return reverse('Clients:Address_Delete', kwargs={'pk': self.id})


class Phone(Model):
    title = CharField(_('Phone Title'), max_length=32)
    phone = CharField(_('Phone Number'), max_length=16)

    # Status
    is_active = BooleanField(_('Is Active?'), default=True)
    is_deleted = BooleanField(_('Is Deleted?'), default=False)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_edit_client_url(self):
        return reverse('Clients:Phone_Edit', kwargs={'pk': self.id})

    def get_delete_client_url(self):
        return reverse('Clients:Phone_Delete', kwargs={'pk': self.id})


class Email(Model):
    title = CharField(_('Email Title'), max_length=32)
    email = EmailField(_('Email Address'), max_length=64)

    # Status
    is_active = BooleanField(_('Is Active?'), default=True)
    is_deleted = BooleanField(_('Is Deleted?'), default=False)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_edit_client_url(self):
        return reverse('Clients:Email_Edit', kwargs={'pk': self.id})

    def get_delete_client_url(self):
        return reverse('Clients:Email_Delete', kwargs={'pk': self.id})


class SocialProfile(Model):
    title = CharField(_('Title'), max_length=64)
    website = URLField(_('Website'), max_length=128, null=True, blank=True)
    linkedin = URLField(_('Linkedin URL'), max_length=2048, null=True, blank=True)
    skype = CharField(_('Skype'), max_length=128, help_text="@username", null=True, blank=True)
    facebook = URLField(_('Facebook URL'), max_length=2048, null=True, blank=True)
    twitter = CharField(_('Twitter'), max_length=128, help_text="@username", null=True, blank=True)
    instagram = CharField(_('Instagram'), max_length=128, help_text="@username", null=True, blank=True)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = _('Social Profile')
        verbose_name_plural = _('Social Profiles')

    def __str__(self):
        return self.title

    def get_edit_client_url(self):
        return reverse('Clients:Social_Edit', kwargs={'pk': self.id})

    def get_delete_client_url(self):
        return reverse('Clients:Social_Delete', kwargs={'pk': self.id})
