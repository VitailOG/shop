from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import (CategorySerializers,
                          ProductSerializers,
                          ProductDetailSerializers
                          )
from product.models import Category, Product


class CategoryAPI(ModelViewSet):
    """Category"""
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class ProductAPI(ReadOnlyModelViewSet):
    """Product"""
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProductSerializers
        elif self.action == "retrieve":
            return ProductDetailSerializers
