from django.contrib import admin
from apps.newsletter.models import Newsletter


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
    