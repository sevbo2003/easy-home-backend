from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from apps.products.models import Category, Product
from apps.products.serializers import CategorySerializer, ProductSerializer, ProductRetrieveSerializer
from apps.products.filters import ProductFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'head', 'options']
    lookup_field = 'slug'

    @action(detail=True, methods=['get'])
    def products(self, request, slug=None):
        category = self.get_object()
        products = category.product_set.all()
        serializer = ProductSerializer(products, many=True)
        pagination = self.paginate_queryset(products)
        if pagination is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'head', 'options']
    filterset_class = ProductFilter
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductRetrieveSerializer
        return ProductSerializer

    @action(detail=False, methods=['get'])
    def featured_products(self, request):
        products = Product.objects.filter(is_featured=True)
        serializer = ProductSerializer(products, many=True)
        pagination = self.paginate_queryset(products)
        if pagination is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    