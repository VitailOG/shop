from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .pagination import ProductPagination
from .filters import ProductFilter
# from .serializers import (CategorySerializers,
#                           ProductSerializers,
#                           ProductDetailSerializers
#                           )
from .serializers import (
    ProductSerializer,
    ProductDetailSerializer
)

from product.models import Category, Product


class ProductAPI(ReadOnlyModelViewSet):
    queryset = Product.objects.all().select_related('category')
    filter_backends = [DjangoFilterBackend]
    pagination_class = ProductPagination
    filterset_class = ProductFilter
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == "list":
            return ProductSerializer
        elif self.action == "retrieve":
            return ProductDetailSerializer


# class CategoryAPI(ModelViewSet):
#     """ Category
#     """
#     serializer_class = CategorySerializers
#     queryset = Category.objects.all()
#
#
# class ProductAPI(ReadOnlyModelViewSet):
#     """ Product
#     """
#     queryset = Product.objects.all()
#     pagination_class = ProductPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = ProductFilterAPI
#
#     def get_serializer_class(self):
#         if self.action == "list":
#             return ProductSerializers
#         elif self.action == "retrieve":
#             return ProductDetailSerializers

