from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, DeleteView, FormView, TemplateView, UpdateView

from rcrm_account.utils import UserAccountControlViewMixin
from rcrm_account.utils import AccountControlViewMixin, AccountControlViewMixinTwo,\
    AccountControlViewMixinThree, AccountControlViewMixinFour
from rcrm_client.forms import ClientForm, ClientContactForm
from rcrm_client.models import Client
from rcrm_contact.models import Contact
from rcrm_contact.forms import ContactForm
from rcrm_util.models import Address, Email, SocialProfile, Phone
from rcrm_util.forms import AddressForm, EmailForm, SocialProfileForm, PhoneForm


# Create your views here.


# --------------------------------- Client ---------------------------------

class ClientListView(UserAccountControlViewMixin, TemplateView):
    """
    Clients are listed with this view.
    """
    template_name = 'client/pages/client_list.html'

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        queryset = Client.objects.filter(is_deleted=False, account=self.request.user.account)
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(Q(name__icontains=q) |
                                       Q(description__icontains=q) |
                                       Q(phone__phone__icontains=q) |
                                       Q(email__email__icontains=q)
                                       )
        context['clients'] = queryset.distinct()
        context['all_clients'] = Client.objects.filter(is_deleted=False, account=self.request.user.account)
        return context


class ClientDetailView(AccountControlViewMixin, TemplateView):
    """
    Client detail information can be seen with this view.
    """
    template_name = 'client/pages/client_detail.html'

    def dispatch(self, request, pk, *args, **kwargs):
        try:
            self.client = Client.objects.get(is_deleted=False, id=pk)
        except Client.DoesNotExist:
            raise Http404()

        if self.client.account != request.user.account:
            return redirect('Clients:Client')

        return super(ClientDetailView, self).dispatch(request, pk, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)

        context.update({
            'client': self.client
        })

        return context


class ClientCreateView(UserAccountControlViewMixin, CreateView):
    """
    A client can be created using this view.
    """
    model = Client
    form_class = ClientForm
    template_name = 'client/forms/client_create.html'
    success_url = reverse_lazy('Clients:Client')

    def form_valid(self, form):
        form_cc = form.save(commit=False)
        form_cc.account = self.request.user.account
        form_cc.save()
        messages.success(self.request, _('Created successfully, thank you.'))
        return super(ClientCreateView, self).form_valid(form)


class ClientEditView(AccountControlViewMixinTwo, UpdateView):
    """
    A client can be edited using this view.
    """
    model = Client
    form_class = ClientForm
    template_name = 'client/forms/client_edit.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        client = get_object_or_404(Client, id=id)
        return reverse('Clients:Client_Detail', args=[client.id])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(ClientEditView, self).form_valid(form)


class ClientDeleteView(AccountControlViewMixinTwo, UpdateView):
    """
    A client can be deleted using this view.
    """
    model = Client
    fields = []
    template_name = 'client/forms/client_delete.html'

    def get_success_url(self):
        return reverse_lazy('Clients:Client')

    def form_valid(self, form):
        form_delete = form.save(commit=False)
        form_delete.is_active = False
        form_delete.is_deleted = True
        form_delete.save()
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(ClientDeleteView, self).form_valid(form=form)


# --------------------------------- Contact ---------------------------------


class ContactAddView(FormView):
    """
    This view creates a contact and adds it into contact field of Client model.
    """
    form_class = ClientContactForm
    template_name = 'client/forms/contact_add.html'

    def get_context_data(self, **kwargs):
        id = self.kwargs['pk']
        context = super(ContactAddView, self).get_context_data(**kwargs)
        context['form_c'] = ContactForm(self.request.POST or None)
        context['client'] = get_object_or_404(Client, id=id)
        return context

    def form_valid(self, form):
        id = self.kwargs['pk']
        client = get_object_or_404(Client, id=id)
        client.contact.add(form.contact)
        messages.success(self.request, _('Added successfully, thank you.'))
        return super(ContactAddView, self).form_valid(form=form)

    def get_form_kwargs(self):
        self.kwargs = super(ContactAddView, self).get_form_kwargs()
        self.kwargs['user'] = self.request.user
        return self.kwargs


class ContactCreateView(CreateView):
    """
    This views allows to create a phone for client.
    """
    model = Contact
    form_class = ContactForm

    def get_success_url(self):
        id = self.kwargs['pk']
        client = get_object_or_404(Client, id=id)
        return reverse('Clients:Client_Detail', args=[client.id])

    def form_valid(self, form):
        id = self.kwargs['pk']
        client = get_object_or_404(Client, id=id)
        form_c = form.save(commit=False)
        form_c.account = self.request.user.account
        client.contact.add(form_c)
        messages.success(self.request, _('Added successfully, thank you.'))
        return super(ContactCreateView, self).form_valid(form=form)


class ContactDeleteView(UpdateView):
    """
    This view removes the contact from related client model.
    """
    model = Client
    fields = []
    template_name = 'client/forms/contact_delete.html'

    def form_valid(self, form):
        contact_id = self.kwargs['contact_id']
        contact = get_object_or_404(Contact, id=contact_id)
        form_delete = form.save(commit=False)
        form_delete.contact.remove(contact)
        messages.success(self.request, _('Removed successfully, thank you.'))
        return super(ContactDeleteView, self).form_valid(form=form)


# --------------------------------- Phone ---------------------------------

class PhoneCreateView(CreateView):
    """
    This views allows to create a phone for client.
    """
    model = Phone
    form_class = PhoneForm
    template_name = 'client/forms/phone_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        client = get_object_or_404(Client, id=id)
        return reverse('Clients:Client_Detail', args=[client.id])

    def form_valid(self, form):
        id = self.kwargs['pk']
        client = get_object_or_404(Client, id=id)
        form_p = form.save(commit=False)
        form_p.title = '%s%s' % (client.name, '\'s Phone Number')
        form_p.save()
        client.phone.add(form_p)
        messages.success(self.request, _('Added successfully, thank you.'))
        return super(PhoneCreateView, self).form_valid(form=form)


class PhoneEditView(UpdateView):
    """
    A phone number can be edited using this view.
    """
    model = Phone
    form_class = PhoneForm
    template_name = 'client/forms/phone_edit.html'

    def get_success_url(self):
        id = self.kwargs['client_id']
        client = get_object_or_404(Client, id=id)
        return reverse('Clients:Client_Detail', args=[client.id])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(PhoneEditView, self).form_valid(form)


class PhoneDeleteView(DeleteView):
    """
    A phone number can be deleted using this view.
    """
    model = Phone
    template_name = 'client/forms/phone_delete.html'

    def get_success_url(self):
        id = self.kwargs['client_id']
        client = get_object_or_404(Client, id=id)
        return reverse('Clients:Client_Detail', args=[client.id])

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(PhoneDeleteView, self).delete(request, *args, **kwargs)


# --------------------------------- Email ---------------------------------

class EmailCreateView(CreateView):
    """
    This views allows to create a email for client.
    """
    model = Email
    form_class = EmailForm
    template_name = 'client/forms/email_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        client = get_object_or_404(Client, id=id)
        return reverse('Clients:Client_Detail', args=[client.id])

    def form_valid(self, form):
        id = self.kwargs['pk']
        client = get_object_or_404(Client, id=id)
        form_e = form.save(commit=False)
        form_e.title = '%s%s' % (client.name, '\'s Address')
        form_e.save()
        client.email.add(form_e)
        messages.success(self.request, _('Added successfully, thank you.'))
        return super(EmailCreateView, self).form_valid(form=form)


class EmailEditView(UpdateView):
    """
    An email can be edited using this view.
    """
    model = Email
    form_class = EmailForm
    template_name = 'client/forms/email_edit.html'

    def get_success_url(self):
        id = self.kwargs['client_id']
        client = get_object_or_404(Client, id=id)
        return reverse('Clients:Client_Detail', args=[client.id])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(EmailEditView, self).form_valid(form)


class EmailDeleteView(DeleteView):
    """
    An email can be deleted using this view.
    """
    model = Email
    template_name = 'client/forms/email_delete.html'

    def get_success_url(self):
        id = self.kwargs['client_id']
        client = get_object_or_404(Client, id=id)
        return reverse('Clients:Client_Detail', args=[client.id])

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(EmailDeleteView, self).delete(request, *args, **kwargs)


# --------------------------------- Address ---------------------------------

class AddressCreateView(CreateView):
    """
    This views allows to create a address for client.
    """
    model = Address
    form_class = AddressForm
    template_name = 'client/forms/address_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        client = get_object_or_404(Client, id=id)
        return reverse('Clients:Client_Detail', args=[client.id])

    def form_valid(self, form):
        id = self.kwargs['pk']
        client = get_object_or_404(Client, id=id)
        form_ad = form.save(commit=False)
        form_ad.title = '%s%s' % (client.name, '\'s Address')
        form_ad.save()
        client.address.add(form_ad)
        messages.success(self.request, _('Added successfully, thank you.'))
        return super(AddressCreateView, self).form_valid(form=form)


class AddressEditView(UpdateView):
    """
    An address can be edited using this view.
    """
    model = Address
    form_class = AddressForm
    template_name = 'client/forms/address_edit.html'

    def get_success_url(self):
        id = self.kwargs['client_id']
        client = get_object_or_404(Client, id=id)
        return reverse('Clients:Client_Detail', args=[client.id])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(AddressEditView, self).form_valid(form)


class AddressDeleteView(DeleteView):
    """
    An address number can be deleted using this view.
    """
    model = Address
    template_name = 'client/forms/address_delete.html'

    def get_success_url(self):
        id = self.kwargs['client_id']
        client = get_object_or_404(Client, id=id)
        return reverse('Clients:Client_Detail', args=[client.id])

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(AddressDeleteView, self).delete(request, *args, **kwargs)


# ------------------------------- Social Profile -------------------------------

class SocialCreateView(CreateView):
    """
    This views allows to create a social profile for client.
    """
    model = SocialProfile
    form_class = SocialProfileForm
    template_name = 'client/forms/social_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        client = get_object_or_404(Client, id=id)
        return reverse('Clients:Client_Detail', args=[client.id])

    def form_valid(self, form):
        id = self.kwargs['pk']
        client = get_object_or_404(Client, id=id)
        form_sp = form.save(commit=False)
        form_sp.title = '%s%s' % (client.name, '\'s Phone Number')
        form_sp.save()
        client.social.add(form_sp)
        messages.success(self.request, _('Added successfully, thank you.'))
        return super(SocialCreateView, self).form_valid(form=form)


class SocialEditView(UpdateView):
    """
    A social profile can be edited using this view.
    """
    model = SocialProfile
    form_class = SocialProfileForm
    template_name = 'client/forms/social_edit.html'

    def get_success_url(self):
        id = self.kwargs['client_id']
        client = get_object_or_404(Client, id=id)
        return reverse('Clients:Client_Detail', args=[client.id])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(SocialEditView, self).form_valid(form)


class SocialDeleteView(DeleteView):
    """
    A social profile can be deleted using this view.
    """
    model = SocialProfile
    template_name = 'client/forms/social_delete.html'

    def get_success_url(self):
        id = self.kwargs['client_id']
        client = get_object_or_404(Client, id=id)
        return reverse('Clients:Client_Detail', args=[client.id])

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(SocialDeleteView, self).delete(request, *args, **kwargs)




