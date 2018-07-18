from django.forms import ModelForm, CharField, DateField, EmailField, URLField, ImageField, \
                        DateInput, Select, TextInput, Textarea, FileInput
from django.utils.translation import ugettext_lazy as _

from rcrm_job.models import Job
from rcrm_contact.utils import COUNTRIES
from rcrm_job.utils import TYPE_OF_EMPLOYMENT

from ckeditor.widgets import CKEditorWidget



class JobForm(ModelForm):
    title = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    short_description = CharField(widget=Textarea(attrs={'class': 'form-control', 'style': "height:150px"}))
    description = CharField(widget=CKEditorWidget())
    type_of_employment = CharField(widget=Select(choices=TYPE_OF_EMPLOYMENT, attrs={'class': 'form-control custom-select'}))

    talent = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    experience = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    education_level = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    language = CharField(widget=TextInput(attrs={'class': 'form-control'}))

    url = URLField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    image = ImageField(required=False, widget=FileInput(attrs={'class': 'form-control', 'style': 'padding: .50rem .75rem;'}))

    office = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    city = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    country = CharField(widget=Select(choices=COUNTRIES, attrs={'class': 'form-control custom-select'}))

    class Meta:
        model = Job
        fields = (
            'title', 'short_description', 'description', 'type_of_employment',
            'talent', 'experience', 'education_level', 'language',
            'url', 'image',
            'office', 'city', 'country'
        )




