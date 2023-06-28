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
    