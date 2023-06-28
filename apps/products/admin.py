from django.contrib import admin
from apps.products.models import Category, Product, Parameter, Document, ProductSliderImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_en', 'name_ru', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ParameterInline(admin.TabularInline):
    model = Parameter
    extra = 1


class ProductSliderImageInline(admin.TabularInline):
    model = ProductSliderImage
    extra = 1


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_en', 'title_ru', 'category', 'price_uzs', 'is_featured', 'is_active', 'created_at')
    list_filter = ('category', 'is_featured', 'is_active', 'created_at')
    list_editable = ('is_featured', 'is_active')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ParameterInline, ProductSliderImageInline, DocumentInline]
