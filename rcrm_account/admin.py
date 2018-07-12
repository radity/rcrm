from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin
from django.core.paginator import Paginator
from django.utils.translation import ugettext_lazy as _

from rcrm_account.models import CRMAccount, CRMAccountRequest, User

from import_export.admin import ImportExportModelAdmin


# Register your models here.


@register(CRMAccount)
class AdminAccount(ImportExportModelAdmin):
    list_display = ('name', 'email', 'phone', 'is_active', 'is_deleted')
    list_filter = ('is_active', 'is_deleted')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('name', 'phone', 'email')
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('name', 'phone', 'email', 'description', 'logo')
        }),
        (_("Status"), {
            'fields': ('is_active', 'is_deleted')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )


@register(User)
class AdminUser(UserAdmin, ImportExportModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'account', 'is_active', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    readonly_fields = ('created_at', 'modified_at', 'last_login')
    search_fields = ('email', 'first_name', 'last_name', 'account__name')
    ordering = ('email',)
    paginator = Paginator
    list_per_page = 50
    add_fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'password', 'first_name', 'last_name', 'account')
        }),
        (_("Status"), {
            'fields': ['is_active', 'is_staff', 'is_superuser']
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at', 'last_login')
        })
    )


@register(CRMAccountRequest)
class AdminAccount(ImportExportModelAdmin):
    list_display = ('account', 'user', 'is_deleted')
    list_filter = ('is_deleted',)
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('account__name', 'user__email')
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('account', 'user', 'is_deleted')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )
