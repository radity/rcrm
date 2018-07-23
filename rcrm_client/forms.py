from django.forms import ModelForm, CharField, DateField, DateInput, EmailField, Select, TextInput, Textarea, URLField, ModelChoiceField
from django.utils.translation import ugettext_lazy as _

from rcrm_client.models import Client
from rcrm_contact.models import Contact

# Create Your Forms Here


class ClientForm(ModelForm):
    """
    This form allows to create/update a client.
    """
    name = CharField(label=_("First Name"), widget=TextInput(attrs={'class': 'form-control'}))
    description = CharField(label=_("Short Description"), required=False,
                            widget=Textarea(attrs={'class': 'form-control', 'style': "height:150px"}))

    class Meta:
        model = Client
        fields = (
            'name',
            'description'
        )

class ClientContactForm(ModelForm):
    contact = ModelChoiceField(queryset=Contact.objects.all(), widget=Select(attrs={'class': 'form-control custom-select'}), empty_label=None)

    class Meta:
        model = Client
        fields = (
            'contact',
        )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ClientContactForm, self).__init__(*args, **kwargs)
        self.fields['contact'].queryset = Contact.objects.filter(account=user.account, is_active=True, is_deleted=False)