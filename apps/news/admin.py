from django.contrib import admin
from apps.news.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'description','image', 'created_at', 'updated_at', 'is_featured', 'slug',)
    list_filter = ('created_at', 'updated_at', 'is_featured', 'slug',)
    search_fields = ('title', 'description', 'slug')
    readonly_fields = ('created_at', 'updated_at',)
    ordering = ('title', 'description', 'content', 'image', 'created_at', 'updated_at', 'is_featured', 'slug',)
    fieldsets = (
        ("Title", {'fields': ('title', 'title_uz', 'title_en', 'title_ru',)}),
        ("Features", {'fields': ('image', 'is_featured')}),
        ("Extra information", {'fields': ('category', 'description_uz', 'description_en', 'description_ru')}),
        ("Content", {'fields': ('content_uz', 'content_en', 'content_ru')}),
        ("Date", {'fields': ('created_at', 'updated_at', 'slug')}),

    )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(News, NewsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_uz','name_ru', 'value')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Category, CategoryAdmin)