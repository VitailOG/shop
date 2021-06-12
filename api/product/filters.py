from django_filters.rest_framework import FilterSet, CharFilter
from product.models import Product


class ProductFilter(FilterSet):

    title = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['title']
