from rest_framework import serializers
from apps.newsletter.models import Newsletter
from apps.contact.validators import validate_uzb_phone_number


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('id', 'phone_number', 'created_at')
        read_only_fields = ('created_at',)

    def validate_phone_number(self, value):
        validate_uzb_phone_number(value)
        return value
    