from django.contrib import admin
from rcrm_key.models import ResetPasswordKey


@admin.register(ResetPasswordKey)
class ResetPasswordKeyAdmin(admin.ModelAdmin):
    fields = ('key', 'is_used', 'user', ('create_date', 'update_date'))
    readonly_fields = ('key', 'is_used', 'user', 'create_date', 'update_date')

    list_display = ('key', 'user', 'create_date', 'update_date', 'is_used')
    list_filter = ('create_date', 'update_date', 'is_used')
    search_fields = ('key', 'user__email', 'user__first_name', 'user__last_name')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True if request.user.is_superuser else False

    def has_delete_permission(self, request, obj=None):
        return True if request.user.is_superuser else False
