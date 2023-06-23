from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from apps.news.models import News, Category
from apps.news.serializers import CategorySerializer, NewsSerializer, NewsRetrieveSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'head', 'options']

    @action(detail=True, methods=['get'])
    def news(self, request, pk=None):
        category = self.get_object()
        news = News.objects.filter(category=category)
        serializer = NewsSerializer(news, many=True)
        pagination = self.paginate_queryset(news)
        if pagination is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    http_method_names = ['get', 'head', 'options']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NewsRetrieveSerializers
        return NewsSerializer

    @action(detail=False, methods=['get'])
    def featured_posts(self, request):
        news = News.objects.filter(is_featured=True)
        serializer = NewsSerializer(news, many=True)
        pagination = self.paginate_queryset(news)
        if pagination is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    