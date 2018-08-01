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
    email = EmailField(label=_("Email"), widget=TextInput())
    password = CharField(label=_("Password"), widget=PasswordInput())

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)

            if not user:
                raise ValidationError(_('Wrong email or password!'))

        return super(LoginForm, self).clean()


class RegisterForm(ModelForm):
    """
    The form is for user registration.
    """
    email = EmailField(label=_("Email"), widget=TextInput())
    password = CharField(label=_("Password"), widget=PasswordInput())
    confirm_password = CharField(
        label=_("Password Confirmation"), widget=PasswordInput()
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        users = User.objects.filter(email=email)

        if users.exists():
            raise ValidationError(_("This email already exists!"))

        return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError(_('Password can not be confirmed!'))

        return confirm_password


class AccountForm(ModelForm):
    """
    A form that creates or updates an account.
    """
    name = CharField(label=_("RCRM Account Name"), widget=TextInput())
    email = EmailField(label=_("RCRM Account Email"), widget=TextInput())
    phone = CharField(
        label=_("RCRM Account Phone Number"), required=False, widget=TextInput()
    )
    description = CharField(
        label=_("RCRM Account Description"), required=False, widget=Textarea()
    )
    logo = ImageField(
        label=_("RCRM Account Logo"), required=False, widget=FileInput()
    )

    class Meta:
        model = CRMAccount
        fields = (
            'name',
            'email',
            'phone',
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
