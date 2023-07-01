from rest_framework import serializers
from apps.news.models import News, Category
from django.conf import settings


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')

    class Meta:
        model = Category
        fields = ('id', 'name', 'posts_count', 'value')
    
    def get_name(self, obj):
        dict = {
            'uz': obj.name_uz,
            'en': obj.name_en,
            'ru': obj.name_ru,
        }
        return dict
        

class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    title = serializers.SerializerMethodField(method_name='get_title')
    description = serializers.SerializerMethodField(method_name='get_description')
    image = serializers.SerializerMethodField(method_name='get_image')
    
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
    
    def get_image(self, obj):
        if obj.image.url[0] == '/':
            return settings.MAIN_DOMAIN + obj.image.url
        return obj.image
    

class NewsRetrieveSerializers(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
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
