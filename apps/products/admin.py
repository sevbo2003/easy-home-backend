from django.contrib import admin
from apps.products.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_en', 'name_ru', 'slug')
    prepopulated_fields = {'slug': ('name',)}