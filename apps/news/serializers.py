from rest_framework import serializers
from apps.news.models import News, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name_uz', 'name_en', 'name_ru')
        