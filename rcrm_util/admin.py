from django.contrib.admin import register
from django.core.paginator import Paginator
from django.utils.translation import ugettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from rcrm_util.models import Address, Email, Phone, SocialProfile

# Register your models here.


@register(Address)
class AdminAddress(ImportExportModelAdmin):
    list_display = ('city', 'state', 'postcode', 'country')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('title', 'address', 'city', 'state', 'postcode', 'country')
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('title', 'address', 'city', 'state', 'postcode', 'country')
        }),
        (_("Status"), {
            'fields': ('is_active', 'is_deleted')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )


@register(Email)
class AdminEmail(ImportExportModelAdmin):
    list_display = ('title', 'email')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('title', 'email')
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('title', 'email')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )


@register(Phone)
class AdminPhone(ImportExportModelAdmin):
    list_display = ('title', 'phone')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('title', 'phone')
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('title', 'phone')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )


@register(SocialProfile)
class AdminSocialProfile(ImportExportModelAdmin):
    list_display = ('title', 'skype', 'twitter', 'instagram')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('title', 'skype', 'twitter', 'instagram', 'website', 'linkedin', 'facebook')
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('title', 'skype', 'twitter', 'instagram', 'website', 'linkedin', 'facebook')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )