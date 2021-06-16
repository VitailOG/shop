from django_filters.rest_framework import FilterSet, CharFilter
from product.models import Product


class ProductFilter(FilterSet):

    spec__value = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['spec__value']
