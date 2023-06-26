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
    
    def create(self, validated_data):
        number = validated_data['phone_number']
        phone_number_token = PhoneToken.objects.filter(phone_number=number).last()
        if phone_number_token:
            if phone_number_token.is_expired:
                phone_number_token.delete()
                return serializers.ValidationError("Phone number is not verified")
            elif not phone_number_token.is_verified:
                return serializers.ValidationError("Phone number is not verified")
            return Contact.objects.create(**validated_data)
        else:
            return serializers.ValidationError("Phone number is not verified")
        