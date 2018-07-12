from django.contrib.admin import register
from django.core.paginator import Paginator
from django.utils.translation import ugettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from rcrm_employee.models import Address, Employee, Email, SocialProfile, Phone

# Register your models here.


@register(Employee)
class AdminEmployee(ImportExportModelAdmin):
    list_display = ('account', 'get_full_name', 'gender', 'is_active', 'is_deleted')
    list_filter = ('is_active', 'is_deleted')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('name', 'account')
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('account', 'first_name', 'last_name', 'gender', 'title', 'date_of_birth', 'description')
        }),
        (_("Emergency Contact"), {
            'fields': ('emergency_contact', 'emergency_phone_number')
        }),
        (_("Status"), {
            'fields': ('is_active', 'is_deleted')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )


@register(Address)
class AdminAddress(ImportExportModelAdmin):
    list_display = ('employee', 'city', 'state', 'postcode', 'country')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('address', 'city', 'state', 'postcode', 'country')
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('employee', 'address', 'map', 'city', 'state', 'postcode', 'country')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )


@register(Email)
class AdminEmail(ImportExportModelAdmin):
    list_display = ('employee', 'email')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('email',)
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('employee', 'email')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )


@register(SocialProfile)
class AdminSocialProfile(ImportExportModelAdmin):
    list_display = ('employee', 'skype', 'twitter', 'instagram')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('skype', 'twitter', 'instagram', 'website', 'linkedin', 'facebook')
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('employee', 'skype', 'twitter', 'instagram', 'website', 'linkedin', 'facebook', 'other')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )


@register(Phone)
class AdminPhone(ImportExportModelAdmin):
    list_display = ('employee', 'phone')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('phone',)
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('employee', 'phone')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )