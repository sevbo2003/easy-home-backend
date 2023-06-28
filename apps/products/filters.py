from django_filters import rest_framework as filters
from apps.products.models import Product


class ProductFilter(filters.FilterSet):
    price_range = filters.RangeFilter(field_name='price_uzs')

    class Meta:
        model = Product
        fields = ['price_range']