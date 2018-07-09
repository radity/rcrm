from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView

from rcrm_account.utils import UserAccountControlViewMixin
from rcrm_contact.forms import AddressForm, ContactForm, EmailForm, PhoneForm, SocialProfileForm
from rcrm_contact.models import Address, Contact, Email, Phone, SocialProfile
from rcrm_contact.resources import ContactResource, ContactImportResource
from rcrm_account.utils import AccountControlViewMixin, AccountControlViewMixinTwo,\
    AccountControlViewMixinThree, AccountControlViewMixinFour

from openpyxl import Workbook
from tablib import Dataset


# Create your views here.


# --------------------------------- Contact ---------------------------------

class ContactListView(UserAccountControlViewMixin, TemplateView):
    """
    Contact persons are listed with this view.
    """
    template_name = 'pages/contact_list.html'

    def get_context_data(self, **kwargs):
        context = super(ContactListView, self).get_context_data(**kwargs)
        queryset = Contact.objects.filter(is_deleted=False, account=self.request.user.account)
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(Q(first_name__icontains=q) |
                                       Q(last_name__icontains=q) |
                                       Q(Contact_Email__email__icontains=q) |
                                       Q(Contact_Address__address__icontains=q) |
                                       Q(Contact_Phone__phone__icontains=q)
                                       )
        context['contacts'] = queryset.distinct()
        context['all_contacts'] = Contact.objects.filter(is_deleted=False, account=self.request.user.account)
        return context


class ContactDetailView(AccountControlViewMixin, TemplateView):
    """
    Contact detail information can be seen with this view.
    """
    template_name = 'pages/contact_detail.html'

    def get_context_data(self, **kwargs):
        id = self.kwargs.get('pk')
        context = super(ContactDetailView, self).get_context_data(**kwargs)
        context['contact'] = get_object_or_404(Contact, is_deleted=False, id=id)
        return context


class ContactCreateView(UserAccountControlViewMixin, CreateView):
    """
    A contact can be created using this view.
    """
    model = Contact
    form_class = ContactForm
    template_name = 'forms/contact_create.html'
    success_url = reverse_lazy('Contacts:Contact')

    def form_valid(self, form):
        form_cc = form.save(commit=False)
        form_cc.account = self.request.user.account
        form_cc.save()
        messages.success(self.request, _('Created successfully, thank you.'))
        return super(ContactCreateView, self).form_valid(form)


class ContactEditView(AccountControlViewMixinTwo, UpdateView):
    """
    A contact can be edited using this view.
    """
    model = Contact
    form_class = ContactForm
    template_name = 'forms/contact_edit.html'

    def get_success_url(self):
        return reverse_lazy('Contacts:Contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(ContactEditView, self).form_valid(form)


class ContactDeleteView(AccountControlViewMixinTwo, UpdateView):
    """
    A contact can be deleted using this view.
    """
    model = Contact
    fields = []
    template_name = 'forms/contact_delete.html'

    def get_success_url(self):
        return reverse_lazy('Contacts:Contact')

    def form_valid(self, form):
        form_delete = form.save(commit=False)
        form_delete.is_active = False
        form_delete.is_deleted = True
        form_delete.save()
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(ContactDeleteView, self).form_valid(form=form)


# --------------------------------- Address ---------------------------------


class AddressCreateView(AccountControlViewMixinFour, CreateView):
    """
    An address can be created using this view.
    """
    model = Address
    form_class = AddressForm
    template_name = 'forms/address_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        contact = get_object_or_404(Contact, id=id)
        return reverse('Contacts:Contact_Detail', args=[contact.id])

    def form_valid(self, form):
        id = self.kwargs.get('pk')
        contact = get_object_or_404(Contact, id=id)
        form_ca = form.save(commit=False)
        form_ca.contact = contact
        form_ca.title = '%s %s%s' % (contact.first_name, contact.last_name, '\'s Address')
        form_ca.save()
        messages.success(self.request, _('Created successfully, thank you.'))
        return super(AddressCreateView, self).form_valid(form)


class AddressEditView(AccountControlViewMixinThree, UpdateView):
    """
    An address can be edited using this view.
    """
    model = Address
    form_class = AddressForm
    template_name = 'forms/address_edit.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        address = get_object_or_404(Address, id=id)
        contact = address.contact
        return reverse('Contacts:Contact_Detail', args=[contact.id])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(AddressEditView, self).form_valid(form)


class AddressDeleteView(AccountControlViewMixinThree, DeleteView):
    """
    An address can be deleted using this view.
    """
    model = Address
    template_name = 'forms/address_delete.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        address = get_object_or_404(Address, id=id)
        contact = address.contact
        return reverse('Contacts:Contact_Detail', args=[contact.id])

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(AddressDeleteView, self).delete(request, *args, **kwargs)

# --------------------------------- Email ---------------------------------


class EmailCreateView(AccountControlViewMixinFour, CreateView):
    """
    An email can be created using this view.
    """
    model = Email
    form_class = EmailForm
    template_name = 'forms/email_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        contact = get_object_or_404(Contact, id=id)
        return reverse('Contacts:Contact_Detail', args=[contact.id])

    def form_valid(self, form):
        id = self.kwargs.get('pk')
        contact = get_object_or_404(Contact, id=id)
        form_ca = form.save(commit=False)
        form_ca.contact = contact
        form_ca.title = '%s %s%s' % (contact.first_name, contact.last_name, '\'s Email Address')
        form_ca.save()
        messages.success(self.request, _('Created successfully, thank you.'))
        return super(EmailCreateView, self).form_valid(form)


class EmailEditView(AccountControlViewMixinThree, UpdateView):
    """
    An email can be edited using this view.
    """
    model = Email
    form_class = EmailForm
    template_name = 'forms/email_edit.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        email = get_object_or_404(Email, id=id)
        contact = email.contact
        return reverse('Contacts:Contact_Detail', args=[contact.id])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(EmailEditView, self).form_valid(form)


class EmailDeleteView(AccountControlViewMixinThree, DeleteView):
    """
    An email can be deleted using this view.
    """
    model = Email
    template_name = 'forms/email_delete.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        email = get_object_or_404(Email, id=id)
        contact = email.contact
        return reverse('Contacts:Contact_Detail', args=[contact.id])

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(EmailDeleteView, self).delete(request, *args, **kwargs)


# --------------------------------- Phone ---------------------------------


class PhoneCreateView(AccountControlViewMixinFour, CreateView):
    """
    A phone number can be created using this view.
    """
    model = Phone
    form_class = PhoneForm
    template_name = 'forms/phone_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        contact = get_object_or_404(Contact, id=id)
        return reverse('Contacts:Contact_Detail', args=[contact.id])

    def form_valid(self, form):
        id = self.kwargs.get('pk')
        contact = get_object_or_404(Contact, id=id)
        form_ca = form.save(commit=False)
        form_ca.contact = contact
        form_ca.title = '%s %s%s' % (contact.first_name, contact.last_name, '\'s Phone Number')
        form_ca.save()
        messages.success(self.request, _('Created successfully, thank you.'))
        return super(PhoneCreateView, self).form_valid(form)


class PhoneEditView(AccountControlViewMixinThree, UpdateView):
    """
    A phone number can be edited using this view.
    """
    model = Phone
    form_class = PhoneForm
    template_name = 'forms/phone_edit.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        phone = get_object_or_404(Phone, id=id)
        contact = phone.contact
        return reverse('Contacts:Contact_Detail', args=[contact.id])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(PhoneEditView, self).form_valid(form)


class PhoneDeleteView(AccountControlViewMixinThree, DeleteView):
    """
    A phone number can be deleted using this view.
    """
    model = Phone
    template_name = 'forms/phone_delete.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        phone = get_object_or_404(Phone, id=id)
        contact = phone.contact
        return reverse('Contacts:Contact_Detail', args=[contact.id])

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(PhoneDeleteView, self).delete(request, *args, **kwargs)

# --------------------------------- Phone ---------------------------------


class SocialProfileCreateView(AccountControlViewMixinFour, CreateView):
    """
    A social profile can be created using this view.
    """
    model = SocialProfile
    form_class = SocialProfileForm
    template_name = 'forms/social_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        contact = get_object_or_404(Contact, id=id)
        return reverse('Contacts:Contact_Detail', args=[contact.id])

    def form_valid(self, form):
        id = self.kwargs.get('pk')
        contact = get_object_or_404(Contact, id=id)
        form_ca = form.save(commit=False)
        form_ca.contact = contact
        form_ca.title = '%s %s%s' % (contact.first_name, contact.last_name, '\'s Social Profile')
        form_ca.save()
        messages.success(self.request, _('Created successfully, thank you.'))
        return super(SocialProfileCreateView, self).form_valid(form)


class SocialProfileEditView(AccountControlViewMixinThree, UpdateView):
    """
    A social profile can be edited using this view.
    """
    model = SocialProfile
    form_class = SocialProfileForm
    template_name = 'forms/social_edit.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        social = get_object_or_404(SocialProfile, id=id)
        contact = social.contact
        return reverse('Contacts:Contact_Detail', args=[contact.id])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(SocialProfileEditView, self).form_valid(form)


class SocialProfileDeleteView(AccountControlViewMixinThree, DeleteView):
    """
    A social profile can be deleted using this view.
    """
    model = SocialProfile
    template_name = 'forms/social_delete.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        social = get_object_or_404(SocialProfile, id=id)
        contact = social.contact
        return reverse('Contacts:Contact_Detail', args=[contact.id])

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(SocialProfileDeleteView, self).delete(request, *args, **kwargs)


# --------------------------------- Import Export ---------------------------------


def contact_import(request):
    if request.method == 'POST':
        person_resource = ContactImportResource()
        dataset = Dataset()
        new_contacts = request.FILES['myfile']
        account_id = request.user.account.id
        imported_data = dataset.load(new_contacts.read())

        wb = Workbook(imported_data)
        print(wb)


        result = person_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)
            messages.success(request, _('Uploaded successfully, thank you.'))
            return HttpResponseRedirect(reverse_lazy('Contacts:Contact'))
        else:
            messages.error(request, _('Could not be uploaded!'))
            return HttpResponseRedirect(reverse_lazy('Contacts:Contact'))
    return render(request, 'import.html')


def contact_export(request):
    contact_resource = ContactResource()
    queryset = Contact.objects.filter(is_deleted=False, is_active=True, account=request.user.account)
    dataset = contact_resource.export(queryset)
    response = HttpResponse(dataset.xls, content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="contacts.xls"'
    return response