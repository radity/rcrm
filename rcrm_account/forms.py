from django.conf import settings
from django.contrib.auth import authenticate
from django.forms import Form, ModelForm,\
    CharField, EmailField, ImageField,\
    PasswordInput, ValidationError,\
    TextInput, Textarea, FileInput,\
    Select
from django.utils.translation import ugettext_lazy as _

from rcrm_account.models import CRMAccount, User


# Create your forms here.


class LoginForm(Form):
    """
    The form is for user login.
    """
    username = CharField(label=_("Username"), widget=TextInput(attrs={'class': "form-control"}))
    password = CharField(label=_("Password"), widget=PasswordInput(attrs={'class': "form-control"}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError(_('Wrong email or password!'))
        return super(LoginForm, self).clean()


class RegisterForm(ModelForm):
    """
    The form is for user registration.
    """
    email = CharField(label=_("Email"), widget=TextInput(attrs={'class': "form-control"}))
    password = CharField(label=_("Password"), widget=PasswordInput(attrs={'class': "form-control"}))
    password2 = CharField(label=_("Password Confirmation"),
                          widget=PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = [
            'email',
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
        return super(RegisterForm, self).clean(*args, **kwargs)


class AccountForm(ModelForm):
    """
    A form that creates or updates an account.
    """
    name = CharField(label=_("Account Name"), widget=TextInput(attrs={'class': 'form-control'}))
    company_email = EmailField(label=_("Account Email"), widget=TextInput(attrs={'class': 'form-control'}))
    company_phone = CharField(label=_("Account Phone Number"), required=False,
                              widget=TextInput(attrs={'class': 'form-control'}))
    description = CharField(label=_("Account Name"), required=False, widget=Textarea(attrs={'class': 'form-control',
                                                                                            'style': "height:150px"}))
    logo = ImageField(required=False, widget=FileInput(attrs={'class': 'form-control', 'style': 'padding: .50rem .75rem;'}))

    class Meta:
        model = CRMAccount
        fields = (
            'name',
            'company_email',
            'company_phone',
            'description',
            'logo'
        )


class AccountUserAddForm(Form):
    """
    The form is for adding a new user
    """
    email = EmailField(label=_("Email Address"),
                       widget=TextInput(attrs={'class': 'form-control', 'placeholder': _("example@email.com")}))


class UserAccountForm(ModelForm):
    """
    A form that lets a user edit own profile
    """
    class Meta:
        model = User
        fields = ()


class AccountRequestForm(Form):
    """
    A form that lets a user to request to an account
    """
    account = CharField(label=_("Account Name"),
                        widget=TextInput(attrs={'class': 'form-control', 'id': 'autocomplete-input'}))


class UserProfileForm(ModelForm):
    """
    A form that lets a user edit own profile
    """
    email = EmailField(label=_("Email"), widget=TextInput(attrs={'class': 'form-control'}))
    first_name = CharField(label=_("First Name"), required=False, widget=TextInput(attrs={'class': 'form-control'}))
    last_name = CharField(label=_("Last Name"), required=False, widget=TextInput(attrs={'class': 'form-control'}))
    language = CharField(label=_("Country"),
                        widget=Select(choices=settings.LANGUAGES, attrs={'class': 'form-control custom-select'}))

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'language'
        )


class SetPasswordForm(ModelForm):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    new_password1 = CharField(
        label=_("New password"),
        widget=PasswordInput(attrs={'class': 'form-control'}),
        strip=False
    )
    new_password2 = CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ()

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.instance.set_password(password)
        if commit:
            self.instance.save()
        return self.instance


class PasswordChangeForm(SetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': _("Your old password was entered incorrectly. Please enter it again."),
    })
    old_password = CharField(
        label=_("Old password"),
        strip=False,
        widget=PasswordInput(attrs={'class': 'form-control'}),
    )

    field_order = ['old_password', 'new_password1', 'new_password2']

    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.instance.check_password(old_password):
            raise ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password
