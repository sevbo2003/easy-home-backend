from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.service.views import ServiceViewSet


router = DefaultRouter()

router.register('', ServiceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
