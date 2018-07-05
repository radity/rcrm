from django.conf import settings
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView, DeleteView, UpdateView


from dal import autocomplete

from rcrm_account.models import Account, AccountRequest, User
from rcrm_account.forms import LoginForm, RegisterForm, UserProfileForm, PasswordChangeForm, \
    AccountForm, AccountUserAddForm, AccountRequestForm
from rcrm_account.utils import AccountControlViewMixin

# Create your views here.

# --------------------------------- Auth ---------------------------------


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'forms/user_login.html'
    success_url = reverse_lazy('Dashboard:Home')

    def form_valid(self, form):
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(self.request, user)
        return super(LoginView, self).form_valid(form)


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'forms/user_registration.html'
    success_url = reverse_lazy('Dashboard:Home')

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.is_active = True
            user.save()
            # User Login After Registration
            user = authenticate(username=user.email, password=password)
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)


# --------------------------------- Profile ---------------------------------


class UserProfileView(UpdateView):
    form_class = UserProfileForm
    template_name = 'pages/user_profile.html'
    success_url = reverse_lazy('Accounts:User_Profile')

    def get_object(self, queryset=None):
        return get_object_or_404(User, id=self.request.user.id)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(UserProfileView, self).form_valid(form=form)

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['password_form'] = PasswordChangeForm(data=self.request.POST, user=self.request.user)
        return context


class ChangePasswordView(UpdateView):
    success_url = reverse_lazy('Accounts:User_Profile')
    

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_object(self, queryset=None):
        return get_object_or_404(User, id=self.request.user.id)

    def get_form_class(self):
        return PasswordChangeForm(data=self.request.POST, user=self.request.user)

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        messages.success(self.request, _('Saved successfully, thank you.'))
        return super(ChangePasswordView, self).form_valid(form=form)


# --------------------------------- Account ---------------------------------


class AccountView(UpdateView):
    """This view is for account screen"""
    template_name = 'pages/account.html'
    success_url = reverse_lazy('Accounts:Account')
    form_class = AccountForm

    def get_object(self):
        if self.request.user.account:
            return get_object_or_404(Account, id=self.request.user.account.id)
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        context['form'] = AccountForm(self.request.POST or None, instance=self.request.user.account)
        context['add_user_for'] = AccountUserAddForm(self.request.POST or None)
        context['account_request_form'] = AccountRequestForm(self.request.POST or None)
        return context

    def form_valid(self, form):
        form_account = form.save()
        user = get_object_or_404(User, id=self.request.user.id)
        if user.account:
            pass
        else:
            User.objects.filter(id=user.id).update(account=form_account)
        return super(AccountView, self).form_valid(form=form)


# --------------------------------- Account User ---------------------------------


class AccountUserCreateView(FormView):
    form_class = AccountUserAddForm
    success_url = reverse_lazy('Accounts:Account')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            if not user.account:
                User.objects.filter(email=email).update(account=self.request.user.account)
                messages.success(self.request, _('Added successfully, thank you.'))
            else:
                messages.error(self.request, _('The user already has an account!'))
                pass
        else:
            messages.error(self.request, _('The user could not be found!'))
        return super(AccountUserCreateView, self).form_valid(form=form)


class UserAccountDeleteView(AccountControlViewMixin, UpdateView):
    model = User
    fields = []
    template_name = 'forms/user_account_delete.html'
    success_url = reverse_lazy('Accounts:Account')

    def form_valid(self, form):
        form_delete = form.save(commit=False)
        form_delete.account = None
        form.save()
        messages.success(self.request, _('Removed successfully, thank you.'))
        return super(UserAccountDeleteView, self).form_valid(form=form)


# --------------------------------- Account Request ---------------------------------


class AccountRequestCreateView(FormView):
    form_class = AccountRequestForm
    success_url = reverse_lazy('Accounts:Account')

    def form_valid(self, form):
        account_name = form.cleaned_data.get('account')
        account = Account.objects.filter(name=account_name).first()
        account_users = User.objects.filter(account=account)
        user = self.request.user
        already_requested = AccountRequest.objects.filter(account=account, user=user).first()
        if account and not already_requested:
            AccountRequest.objects.create(account=account, user=user)
            messages.success(self.request, _('Your request has been sent successfully, thank you.'))

            # Send Email
            from_email = settings.EMAIL_HOST_USER
            subject = _('There is an Access Request to Your RCRM Account!')
            message = str(user.email) + ' requested to be a user of your account to accept/decline keep going on ' \
                                        'the link below.<br<br>' + 'http://127.0.0.1:8000/accounts/'
            recipient_list = []
            for usr in account_users:
                recipient_list.append(usr.email)
            print(recipient_list)
            send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list,
                      fail_silently=False, html_message=message)

        elif account and already_requested:
            messages.error(self.request, _('You have already requested to ' + str(account.name) + '!'))
            pass
        else:
            messages.error(self.request, _('The account could not found!'))
            pass
        return super(AccountRequestCreateView, self).form_valid(form=form)


class AccountRequestAcceptView(AccountControlViewMixin, DeleteView):
    model = AccountRequest
    template_name = 'forms/user_request_accept.html'
    success_url = reverse_lazy('Accounts:Account')

    def delete(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        account_request = get_object_or_404(AccountRequest, id=id)
        User.objects.filter(id=account_request.user.id).update(account=account_request.account)
        usr = get_object_or_404(User, id=account_request.user.id)
        messages.success(self.request, _('Accepted successfully, thank you.'))

        # Send Email
        from_email = settings.EMAIL_HOST_USER
        subject = _('Your Request Has Been Accepted')
        message = _('Your RCRM account request has been accepted. To reach the account: http://127.0.0.1:8000/accounts/')
        recipient_list = [usr.email]
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list,
                  fail_silently=False, html_message=message)
        return super(AccountRequestAcceptView, self).delete(request, *args, **kwargs)


class AccountRequestDeclineView(AccountControlViewMixin, DeleteView):
    model = AccountRequest
    template_name = 'forms/user_request_decline.html'
    success_url = reverse_lazy('Accounts:Account')

    def delete(self, request, *args, **kwargs):

        messages.success(self.request, _('Declined, thank you.'))
        return super(AccountRequestDeclineView, self).delete(request, *args, **kwargs)


class AccountAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Account.objects.none()
        qs = Account.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs