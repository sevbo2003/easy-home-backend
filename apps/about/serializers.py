from rest_framework import serializers
from apps.about.models import Experience, TeamMember
from django.conf import settings


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('years_of_experience', 'happy_clients', 'systems_installed')


class TeamMemberSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(method_name='get_image_url')
    position = serializers.SerializerMethodField(method_name='get_position')
    socials = serializers.SerializerMethodField(method_name='get_socials')

    class Meta:
        model = TeamMember
        fields = ('id', 'name', 'position', 'image', 'socials')

    def get_image_url(self, obj):
        return f'{settings.MAIN_DOMAIN}/{obj.image}'
    
    def get_position(self, obj):
        dict = {
            'uz': obj.position_uz,
            'en': obj.position_en,
            'ru': obj.position_ru,
        }
        return dict
    
    def get_socials(self, obj):
        return [
            {
                'name': 'telegram',
                'url': obj.telegram
            },
            {
                'name': 'instagram',
                'url': obj.instagram
            },
            {
                'name': 'facebook',
                'url': obj.facebook
            }
        ]