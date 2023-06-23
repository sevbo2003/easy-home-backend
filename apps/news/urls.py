from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.news.views import CategoryViewSet, NewsViewSet

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('news', NewsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]