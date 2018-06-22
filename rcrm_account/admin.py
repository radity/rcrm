from django.contrib.admin import register
from django.core.paginator import Paginator
from django.utils.translation import ugettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from .models import Account

# Register your models here.


@register(Account)
class AdminAccount(ImportExportModelAdmin):
    list_display = ('name', 'get_phones', 'get_emails', 'is_active', 'is_deleted')
    list_filter = ('is_active', 'is_deleted')
    readonly_fields = ('created_at', 'modified_at',)
    search_fields = ('name', 'phone',)
    ordering = ('name',)
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('name', 'contact', 'phone', 'email', 'description')
        }),
        (_("Status"), {
            'fields': ('is_active', 'is_deleted')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )

