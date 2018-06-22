from django.db.models import Model, PROTECT, \
    BooleanField, CharField, DateField,\
    DateTimeField, EmailField, ForeignKey,\
    IntegerField, TextField, URLField
from django.utils.translation import ugettext_lazy as _

from location_field.models.plain import PlainLocationField
from rcrm_utils.utils import COUNTRIES

# Create your models here.


class Address(Model):
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

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class SocialProfile(Model):
    title = CharField(_('Social Profile Title'), max_length=32, help_text="Ex: Mr. Ozgur Aksakal's Social Profile")
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

    class Meta:
        verbose_name = _('Social Profile')
        verbose_name_plural = _('Social Profiles')


class Phone(Model):
    title = CharField(_('Phone Title'), max_length=32, help_text="Ex: Mr. Ozgur Aksakal's Phone Number")
    phone = CharField(max_length=16)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    def __str__(self):
        full_name = '%s %s' % (self.title, self.phone)
        return full_name.strip()


class Email(Model):
    title = CharField(_('Email Title'), max_length=32, help_text="Ex: Mr. Ozgur Aksakal's Email Address")
    email = EmailField(max_length=64)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    def __str__(self):
        full_name = '%s %s' % (self.title, self.email)
        return full_name.strip()
