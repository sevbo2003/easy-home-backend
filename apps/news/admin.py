from django.contrib import admin
from apps.news.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'content', 'image', 'created_at', 'updated_at', 'is_featured', 'slug',)
    list_filter = ('created_at', 'updated_at', 'is_featured', 'slug',)
    search_fields = ('title', 'description', 'slug')
    readonly_fields = ('created_at', 'updated_at',)
    ordering = ('title', 'description', 'content', 'image', 'created_at', 'updated_at', 'is_featured', 'slug',)
    fieldsets = (
        (None, {'fields': ('title', 'description', 'content', 'image', 'is_featured', 'slug',)}),
    )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(News, NewsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Category, CategoryAdmin)