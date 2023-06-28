from django.contrib import admin
from apps.service.models import Service, ServiceImage, KeyFeatures


class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1


class KeyFeaturesInline(admin.TabularInline):
    model = KeyFeatures
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_ru', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name_uz', 'name_en', 'name_ru')
    inlines = (ServiceImageInline, KeyFeaturesInline)
    prepopulated_fields = {'slug': ('name',)}
