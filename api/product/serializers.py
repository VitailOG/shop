from rest_framework.relations import SlugRelatedField
from product.models import (Category,
                            Product,
                            Review,
                            ShortImgProduct,
                            Spec
                            )
from rest_framework.serializers import ModelSerializer


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class ReviewSerializers(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ShortImgProductSerializers(ModelSerializer):
    class Meta:
        model = ShortImgProduct
        fields = ('img',)


class SpecSerializers(ModelSerializer):
    class Meta:
        model = Spec
        fields = ('key', 'value')


class ProductDetailSerializers(ModelSerializer):
    """Detail product"""
    category = CategorySerializers()
    review = ReviewSerializers(many=True)
    mdl = ShortImgProductSerializers(many=True)
    spec = SpecSerializers(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializers(ModelSerializer):
    """Product"""
    category = CategorySerializers()

    class Meta:
        model = Product
        fields = '__all__'
