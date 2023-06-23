from rest_framework import serializers
from apps.news.models import News, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name_uz', 'name_en', 'name_ru', 'posts_count',)
        

class NewsSerializer(serializers.ModelSerializer):
    category = serializers.ListSerializer(child=serializers.CharField())
    title = serializers.SerializerMethodField(method_name='get_title')
    description = serializers.SerializerMethodField(method_name='get_description')
    
    class Meta:
        model = News
        fields = ('id', 'category', 'title', 'description', 'image', 'created_at', 'updated_at', 'is_featured', 'slug',)

    def get_title(self, obj):
        dict = {
            'uz': obj.title_uz,
            'en': obj.title_en,
            'ru': obj.title_ru,
        }
        return dict
    
    def get_description(self, obj):
        dict = {
            'uz': obj.description_uz,
            'en': obj.description_en,
            'ru': obj.description_ru,
        }
        return dict


class NewsRetrieveSerializers(serializers.ModelSerializer):
    category = serializers.ListSerializer(child=serializers.CharField())
    title = serializers.SerializerMethodField(method_name='get_title')
    description = serializers.SerializerMethodField(method_name='get_description')
    content = serializers.SerializerMethodField(method_name='get_content')

    class Meta:
        model = News
        fields = ('id', 'category', 'title', 'description', 'image', 'created_at', 'updated_at', 'is_featured', 'slug', 'content')

    def get_title(self, obj):
        dict = {
            'uz': obj.title_uz,
            'en': obj.title_en,
            'ru': obj.title_ru,
        }
        return dict
    
    def get_description(self, obj):
        dict = {
            'uz': obj.description_uz,
            'en': obj.description_en,
            'ru': obj.description_ru,
        }
        return dict

    def get_content(self, obj):
        dict = {
            'uz': obj.content_uz,
            'en': obj.content_en,
            'ru': obj.content_ru,
        }
        return dict
