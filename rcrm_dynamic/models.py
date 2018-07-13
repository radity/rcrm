from django.db.models import Model, CASCADE, \
    BooleanField, CharField, DateField,\
    DateTimeField, FileField, ForeignKey,\
    ImageField, ManyToManyField, TextField,\
    TimeField, URLField
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _

from rcrm_contact.models import Contact

# Create your models here.

# ------------------------------ Fields ------------------------------


class CharfieldModel(Model):
    name = CharField(max_length=32)
    charfield = CharField(max_length=128)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Charfield')


class TextboxModel(Model):
    name = CharField(max_length=32)
    textbox = TextField()

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Text Box')


class ImageModel(Model):
    name = CharField(max_length=32)
    image = ImageField(upload_to='contact_dynamic/image/')

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Image')


class FileModel(Model):
    name = CharField(max_length=32)
    file = FileField(upload_to='contact_dynamic/file/')

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('File')


class DateModel(Model):
    name = CharField(max_length=32)
    date = DateField()

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Date')


class TimeModel(Model):
    name = CharField(max_length=32)
    date = TimeField()

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Time')


class DateTimeModel(Model):
    name = CharField(max_length=32)
    date = DateTimeField()

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Date Time')


class URLModel(Model):
    name = CharField(max_length=32)
    url = URLField(max_length=2048)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('URL')


class BooleanModel(Model):
    name = CharField(max_length=32)
    boolean = BooleanField(default=False)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Boolean')


# ------------------------------ Dynamic Model ------------------------------


class Dynamic(Model):
    name = CharField(max_length=32)
    contact = ForeignKey(Contact, on_delete=CASCADE, related_name='dynamic_app_contact')

    # Dynamic Fields
    charfield = ManyToManyField(CharfieldModel, blank=True)
    text_box = ManyToManyField(TextboxModel, blank=True)
    image = ManyToManyField(ImageModel, blank=True)
    file = ManyToManyField(FileModel, blank=True)
    date = ManyToManyField(DateModel, blank=True)
    time = ManyToManyField(TimeModel, blank=True)
    date_time = ManyToManyField(DateTimeModel, blank=True)
    url = ManyToManyField(URLModel, blank=True)
    yes_no = ManyToManyField(BooleanModel, blank=True)

    # Status
    is_active = BooleanField(_('Is Active?'), default=True)
    is_deleted = BooleanField(_('Is Deleted?'), default=False)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('*Dynamic')

    def get_add_charfield_url(self):
        return reverse('Dynamic:Dynamic_Charfield_Create', kwargs={'pk': self.id})

    def get_add_textbox_url(self):
        return reverse('Dynamic:Dynamic_Textbox_Create', kwargs={'pk': self.id})

    def get_add_image_url(self):
        return reverse('Dynamic:Dynamic_Image_Create', kwargs={'pk': self.id})

    def get_add_file_url(self):
        return reverse('Dynamic:Dynamic_File_Create', kwargs={'pk': self.id})

    def get_add_date_url(self):
        return reverse('Dynamic:Dynamic_Date_Create', kwargs={'pk': self.id})

    def get_add_time_url(self):
        return reverse('Dynamic:Dynamic_Time_Create', kwargs={'pk': self.id})

    def get_add_date_time_url(self):
        return reverse('Dynamic:Dynamic_Date_Time_Create', kwargs={'pk': self.id})



















