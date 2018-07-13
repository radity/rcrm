from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import CreateView

from rcrm_contact.models import Contact
from rcrm_dynamic.models import Dynamic,\
    CharfieldModel, TextboxModel, ImageModel,\
    FileModel, DateModel, DateTimeModel,\
    TimeModel, URLModel, BooleanModel

from rcrm_dynamic.forms import DynamicForm, CharfieldForm, TextboxForm, ImageForm, FileForm, DateForm, TimeForm, DateTimeForm

# Create your views here.

# ------------------------------ Dynamic View ------------------------------


class DynamicCreateView(CreateView):
    model = Dynamic
    form_class = DynamicForm
    template_name = 'forms/dynamic/dynamic_contact_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        contact = get_object_or_404(Contact, id=id)
        return reverse('Contacts:Contact_Detail', args=[contact.id])

    def form_valid(self, form):
        id = self.kwargs.get('pk')
        contact = get_object_or_404(Contact, id=id)
        form_d = form.save(commit=False)
        form_d.contact = contact
        form_d.save()
        return super(DynamicCreateView, self).form_valid(form)


# ------------------------------ Charfield View ------------------------------


class CharfieldCreateView(CreateView):
    model = CharfieldModel
    form_class = CharfieldForm
    template_name = 'forms/dynamic/dynamic_charfield_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        dynamic = get_object_or_404(Dynamic, id=id)
        return reverse('Contacts:Contact_Detail', args=[dynamic.contact.id])

    def form_valid(self, form):
        form_d = form.save()
        obj_id = form_d.id
        id = self.kwargs.get('pk')
        dynamic = get_object_or_404(Dynamic, id=id)
        dynamic.charfield.add(obj_id)
        return super(CharfieldCreateView, self).form_valid(form)


# ------------------------------ Text Box View ------------------------------


class TextBoxCreateView(CreateView):
    model = TextboxModel
    form_class = TextboxForm
    template_name = 'forms/dynamic/dynamic_textbox_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        dynamic = get_object_or_404(Dynamic, id=id)
        return reverse('Contacts:Contact_Detail', args=[dynamic.contact.id])

    def form_valid(self, form):
        form_d = form.save()
        obj_id = form_d.id
        id = self.kwargs.get('pk')
        dynamic = get_object_or_404(Dynamic, id=id)
        dynamic.text_box.add(obj_id)
        return super(TextBoxCreateView, self).form_valid(form)


# ------------------------------ Image View ------------------------------


class ImageCreateView(CreateView):
    model = ImageModel
    form_class = ImageForm
    template_name = 'forms/dynamic/dynamic_image_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        dynamic = get_object_or_404(Dynamic, id=id)
        return reverse('Contacts:Contact_Detail', args=[dynamic.contact.id])

    def form_valid(self, form):
        form_d = form.save()
        obj_id = form_d.id
        id = self.kwargs.get('pk')
        dynamic = get_object_or_404(Dynamic, id=id)
        dynamic.image.add(obj_id)
        return super(ImageCreateView, self).form_valid(form)


# ------------------------------ File View ------------------------------


class FileCreateView(CreateView):
    model = FileModel
    form_class = FileForm
    template_name = 'forms/dynamic/dynamic_file_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        dynamic = get_object_or_404(Dynamic, id=id)
        return reverse('Contacts:Contact_Detail', args=[dynamic.contact.id])

    def form_valid(self, form):
        form_d = form.save()
        obj_id = form_d.id
        id = self.kwargs.get('pk')
        dynamic = get_object_or_404(Dynamic, id=id)
        dynamic.file.add(obj_id)
        return super(FileCreateView, self).form_valid(form)


# ------------------------------ Date View ------------------------------


class DateCreateView(CreateView):
    model = DateModel
    form_class = DateForm
    template_name = 'forms/dynamic/dynamic_date_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        dynamic = get_object_or_404(Dynamic, id=id)
        return reverse('Contacts:Contact_Detail', args=[dynamic.contact.id])

    def form_valid(self, form):
        form_d = form.save()
        obj_id = form_d.id
        id = self.kwargs['pk']
        dynamic = get_object_or_404(Dynamic, id=id)
        dynamic.date.add(obj_id)
        return super(DateCreateView, self).form_valid(form)


# ------------------------------ Time View ------------------------------


class TimeCreateView(CreateView):
    model = TimeModel
    form_class = TimeForm
    template_name = 'forms/dynamic/dynamic_time_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        dynamic = get_object_or_404(Dynamic, id=id)
        return reverse('Contacts:Contact_Detail', args=[dynamic.contact.id])

    def form_valid(self, form):
        form_d = form.save()
        obj_id = form_d.id
        id = self.kwargs['pk']
        dynamic = get_object_or_404(Dynamic, id=id)
        dynamic.time.add(obj_id)
        return super(TimeCreateView, self).form_valid(form)


# ------------------------------ Date Time View ------------------------------


class DateTimeCreateView(CreateView):
    model = DateTimeModel
    form_class = DateTimeForm
    template_name = 'forms/dynamic/dynamic_date_time_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        dynamic = get_object_or_404(Dynamic, id=id)
        return reverse('Contacts:Contact_Detail', args=[dynamic.contact.id])

    def form_valid(self, form):
        form_d = form.save()
        obj_id = form_d.id
        id = self.kwargs['pk']
        dynamic = get_object_or_404(Dynamic, id=id)
        dynamic.date_time.add(obj_id)
        return super(DateTimeCreateView, self).form_valid(form)