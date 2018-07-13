from django.forms import ModelForm, CharField, DateField, DateInput, EmailField, Select, TextInput, Textarea, URLField
from django.utils.translation import ugettext_lazy as _

from rcrm_contact.utils import COUNTRIES, GENDER
from rcrm_contact.models import Address, Contact, Email, Phone, SocialProfile

# Create Your Forms Here


class ContactForm(ModelForm):
    """
    This form allows to create/update a contact person.
    """
    first_name = CharField(label=_("First Name"), widget=TextInput(attrs={'class': 'form-control'}))
    last_name = CharField(label=_("Last Name"), widget=TextInput(attrs={'class': 'form-control'}))
    gender = CharField(label=_("Gender"), widget=Select(choices=GENDER, attrs={'class': 'form-control custom-select'}))
    title = CharField(label=_("Position/Title"), widget=TextInput(attrs={'class': 'form-control'}))
    date_of_birth = DateField(widget=DateInput(attrs={'class': 'form-control',
                                                      'placeholder': 'yyyy-mm-dd', 'type': 'date'}))
    description = CharField(label=_("Short Description"), required=False,
                            widget=Textarea(attrs={'class': 'form-control', 'style': "height:150px"}))

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'gender',
            'title',
            'date_of_birth',
            'description'
        )


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


