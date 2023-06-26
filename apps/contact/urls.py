from django.urls import path
from apps.contact.views import ContactViewSet, PhoneTokenViewSet


urlpatterns = [
    path('', ContactViewSet.as_view({'post': 'create'}), name='contact'),
    path('auth/phone-token/', PhoneTokenViewSet.as_view({'post': 'create'}), name='phone_token'),
    path('auth/phone-token/verify/', PhoneTokenViewSet.as_view({'post': 'verify'}), name='phone_token_verify'),
]
