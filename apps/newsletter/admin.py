from django.contrib import admin
from apps.newsletter.models import Newsletter, Xabarnoma


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'created_at')
    search_fields = ('phone_number',)
    list_filter = ('created_at',)
    readonly_fields = ('phone_number', 'created_at')
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('phone_number', 'created_at')
        }),
    )


@admin.register(Xabarnoma)
class XabarnomaAdmin(admin.ModelAdmin):
    list_display = ('created_at',)
    search_fields = ('message',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('message', 'created_at')
        }),
    )
