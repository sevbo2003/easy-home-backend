from rest_framework import serializers
from apps.products.models import Category, Product, Parameter, ProductSliderImage, Document


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')

    class Meta:
        model = Category
        ref_name = 'ProductsCategory' 
        fields = ['id', 'name', 'products_count', 'slug']
    
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
    
    def to_representation(self, instance):
        return super().to_representation(instance).get('image')


class DocumentSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name')

    class Meta:
        model = Document
        fields = ['name', 'file']
    
    def get_name(self, obj):
        dict = {
            'uz': obj.name_uz,
            'en': obj.name_en,
            'ru': obj.name_ru,
        }
        return dict


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField(method_name='get_title')
    description = serializers.SerializerMethodField(method_name='get_description')
    price_uzs = serializers.SerializerMethodField(method_name='get_price_uzs')
    parameters = ParameterSerializer(many=True)
    slider_images = ProductSliderImageSerializer(many=True)
    documents = DocumentSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'image', 'slug', 'category', 'price_uzs', 'is_featured', 'is_active', 'parameters', 'slider_images', 'documents']
    
    def get_title(self, obj):
        dict = {
            'uz': obj.title_uz,
            'en': obj.title_en,
            'ru': obj.title_ru,
        }
        return dict
    
    def get_description(self, obj):
        dict = {
            'uz': obj.description_uz,
            'en': obj.description_en,
            'ru': obj.description_ru,
        }
        return dict
    
    def get_price_uzs(self, obj):
        return [{
            "currency": "uzs",
            "amount": obj.price_uzs
        }]
    