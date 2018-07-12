from django.contrib.admin import register
from django.core.paginator import Paginator
from django.utils.translation import ugettext_lazy as _

from rcrm_job.models import Job

from import_export.admin import ImportExportModelAdmin


# Register your models here.


@register(Job)
class AdminJob(ImportExportModelAdmin):
    list_display = ('title', 'office', 'city', 'country', 'is_active', 'is_deleted')
    list_filter = ('is_active', 'is_deleted')
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('account_name', 'title')
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('account', 'title', 'description', 'url', 'office', 'city', 'country')
        }),
        (_("Status"), {
            'fields': ('is_active', 'is_deleted')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )