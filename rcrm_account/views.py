from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import FormView

from rcrm_account.forms import LoginForm, RegisterForm

# Create your views here.


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
