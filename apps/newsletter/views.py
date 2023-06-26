from rest_framework.viewsets import ModelViewSet
from apps.newsletter.models import Newsletter
from apps.newsletter.serializers import NewsletterSerializer
from apps.contact.models import PhoneToken
from rest_framework.response import Response
from rest_framework import status


class NewsletterViewSets(ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    http_method_names = ["post"]

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
    