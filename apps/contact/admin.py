from django.contrib import admin
from apps.contact.models import Contact, PhoneToken


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone_number', 'email')
    readonly_fields = ('name', 'phone_number', 'email', 'message', 'created_at')
    fieldsets = (
        ('Contact', {
            'fields': ('name', 'phone_number', 'email', 'message', 'created_at')
        }),
    )


@admin.register(PhoneToken)
class PhoneTokenAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'token', 'created_at', 'expires_at', 'is_verified')
    list_filter = ('created_at', 'expires_at', 'is_verified')
    search_fields = ('phone_number', 'token')
    readonly_fields = ('phone_number', 'token', 'created_at', 'expires_at', 'is_verified')
    fieldsets = (
        ('PhoneToken', {
            'fields': ('phone_number', 'token', 'created_at', 'expires_at', 'is_verified')
        }),
    )
    