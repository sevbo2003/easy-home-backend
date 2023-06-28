from rest_framework import serializers
from apps.service.models import Service, ServiceImage, KeyFeatures


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ('image',)

    def to_representation(self, instance):
        return super().to_representation(instance).get('image')


class KeyFeaturesSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField(method_name='get_title')

    class Meta:
        model = KeyFeatures
        fields = ('id', 'title')

    def get_title(self, obj):
        dict = {
            'uz': obj.title_uz,
            'en': obj.title_en,
            'ru': obj.title_ru,
        }
        return dict
    

class ServiceSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')
    key_features = KeyFeaturesSerializer(many=True)

    class Meta:
        model = Service
        fields = ('id', 'name', 'key_features', 'image', 'slug')

    def get_name(self, obj):
        dict = {
            'uz': obj.name_uz,
            'en': obj.name_en,
            'ru': obj.name_ru,
        }
        return dict


class ServiceRetrieveSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')
    images = ServiceImageSerializer(many=True)
    key_features = KeyFeaturesSerializer(many=True)
    content = serializers.SerializerMethodField(method_name='get_content')

    class Meta:
        model = Service
        fields = ('id', 'name', 'key_features', 'image', 'images', 'content', 'slug')

    def get_name(self, obj):
        dict = {
            'uz': obj.name_uz,
            'en': obj.name_en,
            'ru': obj.name_ru,
        }
        return dict
    

    def get_content(self, obj):
        dict = {
            'uz': obj.content_uz,
            'en': obj.content_en,
            'ru': obj.content_ru,
        }
        return dict
    