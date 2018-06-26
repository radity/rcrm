from django.forms import Form, ModelForm, CharField, PasswordInput, ValidationError, TextInput
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

# Create your forms here.


class LoginForm(Form):
    username = CharField(max_length=254, label=_("Username"), widget=TextInput(attrs={'class': "form-control"}))
    password = CharField(max_length=30, label=_("Password"), widget=PasswordInput(attrs={'class': "form-control"}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError(_('Wrong email or password!'))
        return super(LoginForm, self).clean()


class RegisterForm(ModelForm):
    username = CharField(label=_("Username"), widget=TextInput(attrs={'class': "form-control"}))
    password = CharField(max_length=100, label=_("Password"), widget=PasswordInput(attrs={'class': "form-control"}))
    password2 = CharField(max_length=100, label=_("Password Confirmation"), widget=PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2'
        ]

    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise ValidationError(_('Password can not be confirmed!'))
        return super(RegisterForm, self).clean(*args, **kwargs)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise ValidationError(_("This email already exists!"))
        return super(RegisterForm,self).clean(*args, **kwargs)