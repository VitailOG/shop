from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .pagination import ProductPagination
from .filters import ProductFilter
from .serializers import (
    ProductSerializer,
    ProductDetailSerializer,
    ReviewProductSerializer,
    CategorySerializer
)

from product.models import Category, Product, Review


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


# class ReviewAPI(ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewProductSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
