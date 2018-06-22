from django.contrib.admin import register
from django.core.paginator import Paginator
from django.utils.translation import ugettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from .models import Contact

# Register your models here.


@register(Contact)
class AdminContact(ImportExportModelAdmin):
    list_display = ('get_full_name', 'gender', 'get_emails', 'get_phones', 'is_active', 'is_deleted',)
    list_filter = ('is_active', 'is_deleted',)
    readonly_fields = ('created_at', 'modified_at',)
    search_fields = ('name', 'phone',)
    ordering = ('first_name',)
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'gender', 'title', 'date_of_birth', 'description',)
        }),
        (_("Contact"), {
            'fields': ('address', 'email', 'phone',)
        }),
        (_("Social Profile"), {
            'fields': ('social',)
        }),
        (_("Status"), {
            'fields': ('is_active', 'is_deleted')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )