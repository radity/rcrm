from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView

from rcrm_account.utils import UserAccountControlViewMixin
from rcrm_account.utils import AccountControlViewMixin, AccountControlViewMixinTwo, \
    AccountControlViewMixinSix, AccountControlViewMixinFive
from rcrm_employee.forms import AddressForm, EmployeeForm, EmailForm, PhoneForm, SocialProfileForm
from rcrm_employee.models import Address, Email, Employee, Phone, SocialProfile
from rcrm_employee.resources import EmployeeResource


# Create your views here.


class EmployeeListView(UserAccountControlViewMixin, TemplateView):
    """
    Employee persons are listed with this view.
    """
    template_name = 'employee/pages/employee_list.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        queryset = Employee.objects.filter(is_deleted=False, account=self.request.user.account)
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(Q(first_name__icontains=q) |
                                       Q(last_name__icontains=q) |
                                       Q(Employee_Email__email__icontains=q) |
                                       Q(Employee_Address__address__icontains=q) |
                                       Q(Employee_Phone__phone__icontains=q)
                                       )
        context['employees'] = queryset.distinct()
        context['all_employees'] = Employee.objects.filter(is_deleted=False, account=self.request.user.account)
        return context


class EmployeeDetailView(AccountControlViewMixin, TemplateView):
    """
    Employee detail information can be seen with this view.
    """
    template_name = 'employee/pages/employee_detail.html'

    def get_context_data(self, **kwargs):
        id = self.kwargs.get('pk')
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        employee = get_object_or_404(Employee, is_deleted=False, id=id)
        context['employee'] = employee
        return context


class EmployeeCreateView(UserAccountControlViewMixin, CreateView):
    """
    An employee can be created using this view.
    """
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/forms/employee_create.html'
    success_url = reverse_lazy('Employees:Employee')

    def form_valid(self, form):
        form_cc = form.save(commit=False)
        form_cc.account = self.request.user.account
        form_cc.save()
        messages.success(self.request, _('Created successfully, thank you.'))
        return super(EmployeeCreateView, self).form_valid(form)


class EmployeeEditView(AccountControlViewMixinTwo, UpdateView):
    """
    An employee can be edited using this view.
    """
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/forms/employee_edit.html'

    def get_success_url(self):
        return reverse_lazy('Employees:Employee')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(EmployeeEditView, self).form_valid(form)


class EmployeeDeleteView(AccountControlViewMixinTwo, UpdateView):
    """
    An employee can be deleted using this view.
    """
    model = Employee
    fields = []
    template_name = 'employee/forms/employee_delete.html'

    def get_success_url(self):
        return reverse_lazy('Employees:Employee')

    def form_valid(self, form):
        form_delete = form.save(commit=False)
        form_delete.is_active = False
        form_delete.is_deleted = True
        form_delete.save()
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(EmployeeDeleteView, self).form_valid(form=form)


# --------------------------------- Address ---------------------------------


class AddressCreateView(AccountControlViewMixinFive, CreateView):
    """
    An address can be created using this view.
    """
    model = Address
    form_class = AddressForm
    template_name = 'employee/forms/address_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        employee = get_object_or_404(Employee, id=id)
        return reverse('Employees:Employee_Detail', args=[employee.id])

    def form_valid(self, form):
        id = self.kwargs.get('pk')
        employee = get_object_or_404(Employee, id=id)
        form_ca = form.save(commit=False)
        form_ca.employee = employee
        form_ca.title = '%s %s%s' % (employee.first_name, employee.last_name, '\'s Address')
        form_ca.save()
        messages.success(self.request, _('Created successfully, thank you.'))
        return super(AddressCreateView, self).form_valid(form)


class AddressEditView(AccountControlViewMixinSix, UpdateView):
    """
    An address can be edited using this view.
    """
    model = Address
    form_class = AddressForm
    template_name = 'employee/forms/address_edit.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        address = get_object_or_404(Address, id=id)
        employee = address.employee
        return reverse('Employees:Employee_Detail', args=[employee.id])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(AddressEditView, self).form_valid(form)


class AddressDeleteView(AccountControlViewMixinSix, DeleteView):
    """
    An address can be deleted using this view.
    """
    model = Address
    template_name = 'employee/forms/address_delete.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        address = get_object_or_404(Address, id=id)
        employee = address.employee
        return reverse('Employees:Employee_Detail', args=[employee.id])

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(AddressDeleteView, self).delete(request, *args, **kwargs)

# --------------------------------- Email ---------------------------------


class EmailCreateView(AccountControlViewMixinFive, CreateView):
    """
    An email can be created using this view.
    """
    model = Email
    form_class = EmailForm
    template_name = 'employee/forms/email_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        employee = get_object_or_404(Employee, id=id)
        return reverse('Employees:Employee_Detail', args=[employee.id])

    def form_valid(self, form):
        id = self.kwargs.get('pk')
        employee = get_object_or_404(Employee, id=id)
        form_ca = form.save(commit=False)
        form_ca.employee = employee
        form_ca.title = '%s %s%s' % (employee.first_name, employee.last_name, '\'s Email Address')
        form_ca.save()
        messages.success(self.request, _('Created successfully, thank you.'))
        return super(EmailCreateView, self).form_valid(form)


class EmailEditView(AccountControlViewMixinSix, UpdateView):
    """
    An email can be edited using this view.
    """
    model = Email
    form_class = EmailForm
    template_name = 'employee/forms/email_edit.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        email = get_object_or_404(Email, id=id)
        employee = email.employee
        return reverse('Employees:Employee_Detail', args=[employee.id])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(EmailEditView, self).form_valid(form)


class EmailDeleteView(AccountControlViewMixinSix, DeleteView):
    """
    An email can be deleted using this view.
    """
    model = Email
    template_name = 'employee/forms/email_delete.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        email = get_object_or_404(Email, id=id)
        employee = email.employee
        return reverse('Employees:Employee_Detail', args=[employee.id])

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(EmailDeleteView, self).delete(request, *args, **kwargs)


# --------------------------------- Phone ---------------------------------


class PhoneCreateView(AccountControlViewMixinFive, CreateView):
    """
    A phone number can be created using this view.
    """
    model = Phone
    form_class = PhoneForm
    template_name = 'employee/forms/phone_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        employee = get_object_or_404(Employee, id=id)
        return reverse('Employees:Employee_Detail', args=[employee.id])

    def form_valid(self, form):
        id = self.kwargs.get('pk')
        employee = get_object_or_404(Employee, id=id)
        form_ca = form.save(commit=False)
        form_ca.employee = employee
        form_ca.title = '%s %s%s' % (employee.first_name, employee.last_name, '\'s Phone Number')
        form_ca.save()
        messages.success(self.request, _('Created successfully, thank you.'))
        return super(PhoneCreateView, self).form_valid(form)


class PhoneEditView(AccountControlViewMixinSix, UpdateView):
    """
    A phone number can be edited using this view.
    """
    model = Phone
    form_class = PhoneForm
    template_name = 'employee/forms/phone_edit.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        phone = get_object_or_404(Phone, id=id)
        employee = phone.employee
        return reverse('Employees:Employee_Detail', args=[employee.id])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(PhoneEditView, self).form_valid(form)


class PhoneDeleteView(AccountControlViewMixinSix, DeleteView):
    """
    A phone number can be deleted using this view.
    """
    model = Phone
    template_name = 'employee/forms/phone_delete.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        phone = get_object_or_404(Phone, id=id)
        employee = phone.employee
        return reverse('Employees:Employee_Detail', args=[employee.id])

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(PhoneDeleteView, self).delete(request, *args, **kwargs)

# --------------------------------- Phone ---------------------------------


class SocialProfileCreateView(AccountControlViewMixinFive, CreateView):
    """
    A social profile can be created using this view.
    """
    model = SocialProfile
    form_class = SocialProfileForm
    template_name = 'employee/forms/social_create.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        employee = get_object_or_404(Employee, id=id)
        return reverse('Employees:Employee_Detail', args=[employee.id])

    def form_valid(self, form):
        id = self.kwargs.get('pk')
        employee = get_object_or_404(Employee, id=id)
        form_ca = form.save(commit=False)
        form_ca.employee = employee
        form_ca.title = '%s %s%s' % (employee.first_name, employee.last_name, '\'s Social Profile')
        form_ca.save()
        messages.success(self.request, _('Created successfully, thank you.'))
        return super(SocialProfileCreateView, self).form_valid(form)


class SocialProfileEditView(AccountControlViewMixinSix, UpdateView):
    """
    A social profile can be edited using this view.
    """
    model = SocialProfile
    form_class = SocialProfileForm
    template_name = 'employee/forms/social_edit.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        social = get_object_or_404(SocialProfile, id=id)
        employee = social.employee
        return reverse('Employees:Employee_Detail', args=[employee.id])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(SocialProfileEditView, self).form_valid(form)


class SocialProfileDeleteView(AccountControlViewMixinSix, DeleteView):
    """
    A social profile can be deleted using this view.
    """
    model = SocialProfile
    template_name = 'employee/forms/social_delete.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        social = get_object_or_404(SocialProfile, id=id)
        employee = social.employee
        return reverse('Employees:Employee_Detail', args=[employee.id])

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(SocialProfileDeleteView, self).delete(request, *args, **kwargs)


# --------------------------------- Import Export ---------------------------------


def employee_export(request):
    employee_resource = EmployeeResource()
    queryset = Employee.objects.filter(is_deleted=False, is_active=True, account=request.user.account)
    dataset = employee_resource.export(queryset)
    response = HttpResponse(dataset.xls, content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="employees.xls"'
    return response