from django.forms import ModelForm, CharField, DateField, EmailField, URLField, ImageField, \
                        DateInput, Select, TextInput, Textarea, FileInput
from django.utils.translation import ugettext_lazy as _

from rcrm_job.models import Job
from rcrm_contact.utils import COUNTRIES
from rcrm_job.utils import TYPE_OF_EMPLOYMENT

from ckeditor.widgets import CKEditorWidget



class JobForm(ModelForm):
    title = CharField(label=_('Title'), widget=TextInput())
    short_description = CharField(label=_('Short Description'), widget=Textarea())
    description = CharField(label=_('Description'), widget=CKEditorWidget())
    type_of_employment = CharField(
        label=_('Type of Employment'), widget=Select(choices=TYPE_OF_EMPLOYMENT)
    )

    talent = CharField(label=_('Talent'), widget=TextInput())
    experience = CharField(label=_('Experience'), widget=TextInput())
    education_level = CharField(label=_('Education Level'), widget=TextInput())
    language = CharField(label=_('Language'), widget=TextInput())

    url = URLField(label=_('Detail URL'), required=False, widget=TextInput())
    image = ImageField(label=_('Image'), required=False, widget=FileInput())

    office = CharField(label=_('Office'), widget=TextInput())
    city = CharField(label=_('City'), widget=TextInput())
    country = CharField(label=_('Country'), widget=Select(choices=COUNTRIES))

    class Meta:
        model = Job
        fields = (
            'title', 'short_description', 'description', 'type_of_employment',
            'talent', 'experience', 'education_level', 'language', 'url',
            'image', 'office', 'city', 'country'
        )
