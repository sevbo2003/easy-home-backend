from rest_framework import serializers
from apps.products.models import Category, Product, Parameter, ProductSliderImage, Document


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')

    class Meta:
        model = Category
        ref_name = 'ProductsCategory' 
        fields = ['id', 'name', 'slug']
    
    def get_name(self, obj):
        dict = {
            'uz': obj.name_uz,
            'en': obj.name_en,
            'ru': obj.name_ru,
        }
        return dict


class ParameterSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')

    class Meta:
        model = Parameter
        fields = ['name', 'value']

    def get_name(self, obj):
        dict = {
            'uz': obj.name_uz,
            'en': obj.name_en,
            'ru': obj.name_ru,
        }
        return dict


class ProductSliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSliderImage
        fields = ['image']
