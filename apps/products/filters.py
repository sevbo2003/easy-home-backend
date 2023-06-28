from django_filters import rest_framework as filters
from apps.products.models import Product


class ProductFilter(filters.FilterSet):
    price_range = filters.RangeFilter(field_name='price_uzs')
    search = filters.CharFilter(method='search_filter')

    class Meta:
        model = Product
        fields = ['price_range', 'search']

    def search_filter(self, queryset, name, value):
        return queryset.filter(title_uz__icontains=value) | queryset.filter(title_en__icontains=value) | queryset.filter(title_ru__icontains=value)
    