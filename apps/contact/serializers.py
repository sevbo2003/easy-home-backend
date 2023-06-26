from rest_framework import serializers
from apps.contact.models import Contact, PhoneToken
from apps.contact.validators import validate_uzb_phone_number


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email', 'message']
    
    def validate_phone_number(self, value):
        validate_uzb_phone_number(value)
        return value


class PhoneTokenCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneToken
        fields = ['phone_number']

    def validate(self, attrs):
        data = super().validate(attrs)
        validate_uzb_phone_number(data.get('phone_number', None))
        return data
    