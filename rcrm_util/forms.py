from django.forms import ModelForm, CharField, DateField, DateInput, EmailField, Select, TextInput, Textarea, URLField
from django.utils.translation import ugettext_lazy as _

from rcrm_util.utils import COUNTRIES
from rcrm_util.models import Address, Email, Phone, SocialProfile

# Create Your Forms Here


class AddressForm(ModelForm):
    """
    With this form an address can be created ot updated.
    """
    address = CharField(label=_("Address"), widget=TextInput(attrs={'class': 'form-control'}))
    city = CharField(label=_("City"), widget=TextInput(attrs={'class': 'form-control'}))
    state = CharField(label=_("State"), widget=TextInput(attrs={'class': 'form-control'}))
    postcode = CharField(label=_("Post Code"), widget=TextInput(attrs={'class': 'form-control'}))
    country = CharField(label=_("Country"), widget=Select(choices=COUNTRIES, attrs={'class': 'form-control custom-select'}))

    class Meta:
        model = Address
        fields = (
            'address',
            'city',
            'state',
            'postcode',
            'country'
        )


class EmailForm(ModelForm):
    """
    With this form an email can be created ot updated.
    """
    email = EmailField(label=_("Email"), widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Email
        fields = (
            'email',
        )


class PhoneForm(ModelForm):
    """
    With this form a phone number can be created ot updated.
    """
    phone = CharField(label=_("Phone"), widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Phone
        fields = (
            'phone',
        )


class SocialProfileForm(ModelForm):
    """
    With this form a social profile can be created ot updated.
    """
    skype = CharField(label=_("Skype"), required=False, widget=TextInput(attrs={'class': 'form-control'}))
    twitter = CharField(label=_("Twitter"), required=False, widget=TextInput(attrs={'class': 'form-control'}))
    instagram = CharField(label=_("Instagram"), required=False, widget=TextInput(attrs={'class': 'form-control'}))
    website = URLField(label=_("Website"), required=False, widget=TextInput(attrs={'class': 'form-control'}))
    linkedin = URLField(label=_("Linkedin"), required=False, widget=TextInput(attrs={'class': 'form-control'}))
    facebook = URLField(label=_("Facebook"), required=False, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = SocialProfile
        fields = (
            'skype',
            'twitter',
            'instagram',
            'website',
            'linkedin',
            'facebook'
        )


