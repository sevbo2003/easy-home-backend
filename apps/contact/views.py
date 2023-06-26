from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from apps.contact.models import Contact, PhoneToken
from apps.contact.serializers import ContactSerializer, PhoneTokenCreateSerializer, PhoneTokenVerifySerializer
from apps.contact.utils import generate_token, verify_token
# from apps.contact.tasks import send_background_sms
from core.eskiz import eskiz


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny, ]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data.get('phone_number')
        number = PhoneToken.objects.filter(phone_number=phone).last()
        if number:
            if number.is_verified:
                user = serializer.save()
                number.delete()
                return Response({'status': 'success', 'message': 'Your message has been sent successfully'}, status=status.HTTP_201_CREATED)
            return Response({'status': 'error', 'message': 'Phone number is not verified'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'error', 'message': 'Phone number is not verified'}, status=status.HTTP_400_BAD_REQUEST)
