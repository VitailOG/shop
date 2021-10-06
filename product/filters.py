from django_filters import FilterSet, CharFilter

from .models import Product


class ProductFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ('title',)
