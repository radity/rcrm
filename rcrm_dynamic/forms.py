from django.forms import ModelForm,\
    CharField, DateField, DateInput,\
    EmailField, ImageField, Select,\
    TextInput, Textarea, URLField,\
    FileInput, FileField, TimeField,\
    TimeInput, DateTimeField, DateTimeInput
from django.utils.translation import ugettext_lazy as _

from rcrm_dynamic.models import Dynamic,\
    CharfieldModel, TextboxModel, ImageModel,\
    FileModel, DateModel, DateTimeModel,\
    TimeModel, URLModel, BooleanModel


# Create Your Forms Here

class DynamicForm(ModelForm):
    name = CharField(widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Dynamic
        fields = (
            'name',
        )


class CharfieldForm(ModelForm):
    name = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    charfield = CharField(widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CharfieldModel
        fields = (
            'name',
            'charfield'
        )


class TextboxForm(ModelForm):
    name = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    textbox = CharField(widget=Textarea(attrs={'class': 'form-control','style': "height:150px"}))

    class Meta:
        model = TextboxModel
        fields = (
            'name',
            'textbox'
        )


class ImageForm(ModelForm):
    name = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    image = ImageField(widget=FileInput(attrs={'class': 'form-control', 'style': 'padding: .50rem .75rem;'}))

    class Meta:
        model = ImageModel
        fields = (
            'name',
            'image'
        )


class FileForm(ModelForm):
    name = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    file = FileField(widget=FileInput(attrs={'class': 'form-control', 'style': 'padding: .50rem .75rem;'}))

    class Meta:
        model = FileModel
        fields = (
            'name',
            'file'
        )


class DateForm(ModelForm):
    name = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    date = DateField(widget=DateInput(attrs={'class': 'form-control',
                                                      'placeholder': 'yyyy-mm-dd', 'type': 'date'}))

    class Meta:
        model = DateModel
        fields = (
            'name',
            'date'
        )


class TimeForm(ModelForm):
    name = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    date = TimeField(widget=TimeInput(attrs={'class': 'form-control', 'type': 'time'}))

    class Meta:
        model = TimeModel
        fields = (
            'name',
            'date'
        )


class DateTimeForm(ModelForm):
    name = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    date = DateTimeField(widget=DateTimeInput(attrs={'class': 'form-control'}))

    class Meta:
        model = DateTimeModel
        fields = (
            'name',
            'date'
        )































