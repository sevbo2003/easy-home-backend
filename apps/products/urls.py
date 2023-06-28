from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.products.views import CategoryViewSet, ProductViewSet


router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='categories')
router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]