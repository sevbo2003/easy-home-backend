from rest_framework import serializers
from apps.about.models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('years_of_experience', 'happy_clients', 'systems_installed')
