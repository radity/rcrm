from django.contrib.admin import register
from django.core.paginator import Paginator
from django.utils.translation import ugettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from rcrm_contact.models import Address, Contact, Email, SocialProfile, Phone

# Register your models here.


@register(Contact)
class AdminContact(ImportExportModelAdmin):
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
        (_("Status"), {
            'fields': ('is_active', 'is_deleted')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )


@register(Address)
class AdminAddress(ImportExportModelAdmin):
    list_display = ('title', 'contact', 'city', 'state', 'postcode', 'country')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('title', 'address', 'city', 'state', 'postcode', 'country')
    ordering = ('title',)
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('title', 'contact', 'address', 'map', 'city', 'state', 'postcode', 'country')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )


@register(Email)
class AdminEmail(ImportExportModelAdmin):
    list_display = ('title', 'contact', 'email')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('title', 'email')
    ordering = ('title',)
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('title', 'contact', 'email')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )


@register(SocialProfile)
class AdminSocialProfile(ImportExportModelAdmin):
    list_display = ('title', 'contact', 'skype', 'twitter', 'instagram')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('title', 'skype', 'twitter', 'instagram', 'website', 'linkedin', 'facebook')
    ordering = ('title',)
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('title', 'contact', 'skype', 'twitter', 'instagram', 'website', 'linkedin', 'facebook')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )


@register(Phone)
class AdminPhone(ImportExportModelAdmin):
    list_display = ('title', 'contact', 'phone')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('title', 'phone')
    ordering = ('title',)
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('title', 'contact', 'phone')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )