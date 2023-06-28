from rest_framework import serializers
from apps.service.models import Service, ServiceImage, KeyFeatures


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ('image',)

        def to_representation(self, instance):
            return super().to_representation(instance).get('image')
