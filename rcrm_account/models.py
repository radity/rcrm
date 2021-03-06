from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import Model, CASCADE, PROTECT, \
    BooleanField, CharField, DateTimeField,\
    EmailField, ForeignKey, ImageField,\
    TextField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from rcrm_account.managers import UserManager


# Create your models here.


class CRMAccount(Model):
    """
    This model is crm account that is controlled by many users.
    """
    name = CharField(_('Name'), max_length=64)
    email = EmailField(_('Email'), max_length=2014)
    phone = CharField(_('Phone Number'), max_length=128, null=True, blank=True)
    description = TextField(_('Description'), max_length=256, null=True, blank=True)
    logo = ImageField(_('Logo'), upload_to='logo/', null=True, blank=True)

    # Status
    is_active = BooleanField(_('Is Active?'), default=True)
    is_deleted = BooleanField(_('Is Deleted?'), default=False)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('CRM Account')

    def __str__(self):
        return self.name

    def users(self):
        return User.objects.filter(account=self)

    def requests(self):
        return CRMAccountRequest.objects.filter(account=self, is_deleted=False)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Auth user model.
    """
    email = EmailField(_('Email address'), unique=True)
    first_name = CharField(_('First name'), max_length=30, blank=True)
    last_name = CharField(_('Last name'), max_length=30, blank=True)
    account = ForeignKey(CRMAccount, on_delete=PROTECT, null=True, blank=True)
    language = CharField(max_length=2, choices=settings.LANGUAGES, default='en')

    # Status
    is_active = BooleanField(_('Is Active?'), default=True)
    is_staff = BooleanField(_('Is Staff?'), default=True)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_delete_url(self):
        return reverse('Accounts:User_Delete', kwargs={'pk': self.id})


class CRMAccountRequest(Model):
    """
    With this model users can be added to CRM Accounts.
    """
    account = ForeignKey(CRMAccount, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)

    # Status
    is_deleted = BooleanField(_('Is Deleted?'), default=False)

    # Date & Time
    created_at = DateTimeField(_('Added'), auto_now_add=True)
    modified_at = DateTimeField(_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ('account__name', 'user__first_name')
        verbose_name = _('CRM Account Request')

    def __str__(self):
        str = '%s %s' % (self.account.name, self.user.email)
        return str.strip()

    def get_absolute_url(self):
        return reverse('Accounts:Request_Accept', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('Accounts:Request_Decline', kwargs={'pk': self.id})

