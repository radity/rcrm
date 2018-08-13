import json
from django.conf import settings
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, FormView, DeleteView, UpdateView

from rcrm.modules import KeyModule, MailModule
from rcrm_account.models import CRMAccount, CRMAccountRequest, User
from rcrm_account.forms import (LoginForm, RegisterForm, ForgotPasswordForm, ResetPasswordForm, UserProfileForm,
                                PasswordChangeForm, AccountForm, AccountUserAddForm, AccountRequestForm)
from rcrm_account.utils import AccountControlViewMixin

# Create your views here.

# --------------------------------- Auth ---------------------------------


class LoginView(FormView):
    """
    The view is for user login.
    """
    form_class = LoginForm
    template_name = 'account/forms/user_login.html'
    success_url = reverse_lazy('Dashboard:Home')

    def form_valid(self, form):
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            login(self.request, user)
        return super(LoginView, self).form_valid(form)


class RegisterView(FormView):
    """
    The view is for user registration.
    """
    form_class = RegisterForm
    template_name = 'account/forms/user_registration.html'
    success_url = reverse_lazy('Accounts:Account')

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
            messages.success(self.request, _('You need to join to an account or create an account to use RCRM!'))
        return super(RegisterView, self).form_valid(form)


class ForgotPasswordView(TemplateView):
    template_name = 'account/forms/user_forgot_password.html'

    def get_context_data(self, **kwargs):
        context = super(ForgotPasswordView, self).get_context_data(**kwargs)

        context.update({
            'forgot_password_form': ForgotPasswordForm(prefix='forgot-password-form')
        })

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if 'forgot-password-form' in request.POST:
            forgot_password_form = ForgotPasswordForm(request.POST, prefix='forgot-password-form')

            if forgot_password_form.is_valid():
                user = forgot_password_form.user

                if user:
                    # Send Email
                    MailModule.send_forgot_password_mail(user, request)

                forgot_password_form = ForgotPasswordForm(prefix='forgot-password-form')
                messages.success(request, _('If you have an account we have sent you an email.'))

            context.update({'forgot_password_form': forgot_password_form})

        return super(ForgotPasswordView, self).render_to_response(context)


class ResetPasswordView(TemplateView):
    template_name = 'account/forms/user_reset_password.html'

    def dispatch(self, request, key, *args, **kwargs):
        self.reset_password_key = KeyModule.get_reset_password_key(key)

        if not self.reset_password_key:
            raise Http404()

        return super(ResetPasswordView, self).dispatch(request, key, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ResetPasswordView, self).get_context_data(**kwargs)

        context.update({
            'reset_password_key': self.reset_password_key,
            'reset_password_form': ResetPasswordForm(prefix='reset-password-form')
        })

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if 'reset-password-form' in request.POST:
            reset_password_form = ResetPasswordForm(self.request.POST, prefix='reset-password-form')

            if reset_password_form.is_valid():
                user = reset_password_form.save(self.reset_password_key)

                if user:
                    messages.success(request, _('Your password has been successfully changed.'))
                    return HttpResponseRedirect(reverse('Accounts:Login'))

            context.update({
                'reset_password_form': reset_password_form,
            })

        return super(ResetPasswordView, self).render_to_response(context)


# --------------------------------- Profile ---------------------------------


class ProfileView(TemplateView):
    template_name = 'account/pages/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)

        context.update({
            'form': UserProfileForm(instance=self.request.user, prefix='form'),
            'password_form': PasswordChangeForm(prefix='password-form')
        })

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if 'form' in request.POST:
            form = UserProfileForm(request.POST, instance=request.user, prefix='form')

            if form.is_valid():
                form.save(user=request.user)
                messages.success(self.request, _('Saved successfully, thank you.'))
                translation.activate(request.user.language)

            context.update({'form': form})

        if "password-form" in request.POST:
            password_form = PasswordChangeForm(
                request.POST, instance=request.user, prefix='password-form'
            )

            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(self.request, password_form.instance)
                user = authenticate(email=self.request.user.email, password=self.request.user.password)
                login(self.request, user)

                messages.success(self.request, _('Saved successfully, thank you.'))
            else:
                context.update({'password_form': password_form})

        return super(ProfileView, self).render_to_response(context)


# --------------------------------- Account ---------------------------------


class AccountView(UpdateView):
    """
    Every account actions can be made with this view.
    """
    template_name = 'account/pages/account.html'
    success_url = reverse_lazy('Accounts:Account')
    form_class = AccountForm

    def get_object(self):
        if self.request.user.account:
            return get_object_or_404(CRMAccount, id=self.request.user.account.id)
        else:
            return None

    def get_context_data(self, **kwargs):
        accounts = CRMAccount.objects.filter(is_active=True, is_deleted=False)
        account_list = [account.name for account in accounts]
        context = super(AccountView, self).get_context_data(**kwargs)
        context['form'] = AccountForm(self.request.POST or None, instance=self.request.user.account)
        context['add_user_form'] = AccountUserAddForm(self.request.POST or None)
        context['account_request_form'] = AccountRequestForm(self.request.POST or None)
        context['account_list'] = account_list
        return context

    def form_valid(self, form):
        if form.is_valid():
            form_account = form.save()
            logo = self.request.FILES.get('logo', None)
            if logo:
                form_account.logo = logo
                form_account.save()

            user = get_object_or_404(User, id=self.request.user.id)
            if user.account:
                pass
            else:
                User.objects.filter(id=user.id).update(account=form_account)

        return super(AccountView, self).form_valid(form=form)


# --------------------------------- Account User ---------------------------------


class AccountUserCreateView(FormView):
    """
    With this view a user can be added to the account.
    """
    form_class = AccountUserAddForm
    success_url = reverse_lazy('Accounts:Account')

    def form_valid(self, form):
        email = form.cleaned_data.get('email', None)
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

    def form_invalid(self, form):
        messages.error(self.request, _('Enter a valid email address.'))

        return HttpResponseRedirect(reverse('Accounts:Account'))


class UserAccountDeleteView(AccountControlViewMixin, UpdateView):
    """
    With this view a user can be deleted from an account.
    """
    model = User
    fields = []
    template_name = 'account/forms/user_account_delete.html'
    success_url = reverse_lazy('Accounts:Account')

    def form_valid(self, form):
        form_delete = form.save(commit=False)
        form_delete.account = None
        form.save()
        messages.success(self.request, _('Removed successfully, thank you.'))
        return super(UserAccountDeleteView, self).form_valid(form=form)


# --------------------------------- Account Request ---------------------------------


class AccountRequestCreateView(FormView):
    """
    With this view a user can be applied to be a user of an account to the account.
    """
    form_class = AccountRequestForm
    success_url = reverse_lazy('Accounts:Account')

    def form_valid(self, form):
        account_name = form.cleaned_data.get('account')
        account = CRMAccount.objects.filter(name=account_name).first()
        account_users = User.objects.filter(account=account)
        user = self.request.user
        already_requested = CRMAccountRequest.objects.filter(account=account, user=user).first()
        if account and not already_requested:
            CRMAccountRequest.objects.create(account=account, user=user)
            messages.success(self.request, _('Your request has been sent successfully, thank you.'))

            # Send Email
            MailModule.send_account_request_create_mail(account_users, user, self.request)
        elif account and already_requested:
            messages.error(self.request, _('You have already requested to ' + str(account.name) + '!'))
        else:
            messages.error(self.request, _('The account could not found!'))
        return super(AccountRequestCreateView, self).form_valid(form=form)


class AccountRequestAcceptView(AccountControlViewMixin, DeleteView):
    """
    With this view users of an account can accept the user who has applied before.
    """
    model = CRMAccountRequest
    template_name = 'account/forms/user_request_accept.html'
    success_url = reverse_lazy('Accounts:Account')

    def delete(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        account_request = get_object_or_404(CRMAccountRequest, id=id)
        user = get_object_or_404(User, id=account_request.user.id)
        if user.account:
            messages.error(self.request, _('The user has an account!'))
            return HttpResponseRedirect(reverse_lazy('Accounts:Account'))
        else:
            User.objects.filter(id=account_request.user.id).update(account=account_request.account)
            messages.success(self.request, _('Accepted successfully, thank you.'))

            # Send Email
            MailModule.send_account_request_accept_mail(user, request)

        return super(AccountRequestAcceptView, self).delete(request, *args, **kwargs)


class AccountRequestDeclineView(AccountControlViewMixin, DeleteView):
    """
    With this view users of an account can decline the user who has applied before.
    """
    model = CRMAccountRequest
    template_name = 'account/forms/user_request_decline.html'
    success_url = reverse_lazy('Accounts:Account')

    def delete(self, request, *args, **kwargs):

        messages.success(self.request, _('Declined, thank you.'))
        return super(AccountRequestDeclineView, self).delete(request, *args, **kwargs)
