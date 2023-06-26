from django.contrib import admin
from apps.contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone_number', 'email')
    readonly_fields = ('name', 'phone_number', 'email', 'message', 'created_at')
    fieldsets = (
        ('Contact', {
            'fields': ('name', 'phone_number', 'email', 'message', 'created_at')
        }),
    )
    