from rest_framework.relations import SlugRelatedField
from product.models import (Category,
                            Product,
                            Review,
                            ShortImgProduct,
                            Spec
                            )
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class ImageProductSerializers(ModelSerializer):
    class Meta:
        model = ShortImgProduct
        fields = ('img',)


class SpecProductSerializer(ModelSerializer):

    class Meta:
        model = Spec
        fields = ('key', 'value')


class ReviewProductSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = ('review', 'date', 'user')


class ProductSerializer(ModelSerializer):

    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(ModelSerializer):

    category = CategorySerializer()
    mdl = ImageProductSerializers(many=True)
    spec = SpecProductSerializer(many=True)
    review = ReviewProductSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        lookup_field = 'slug'
