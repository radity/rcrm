from django.contrib.admin import register
from django.core.paginator import Paginator
from django.utils.translation import ugettext_lazy as _

from rcrm_client.models import Client

from import_export.admin import ImportExportModelAdmin

# Register your models here.


@register(Client)
class AdminClient(ImportExportModelAdmin):
    list_display = ('account', 'name', 'get_phones', 'get_emails')
    list_filter = ('is_active', 'is_deleted')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('name',)
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('account', 'name', 'description')
        }),
        (_("Contact Person"), {
            'fields': ('contact',)
        }),
        (_("Contact"), {
            'fields': ('phone', 'email', 'address', 'social')
        }),
        (_("Status"), {
            'fields': ('is_active', 'is_deleted')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )