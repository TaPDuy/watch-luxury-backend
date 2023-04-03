from rest_framework import serializers

from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):

    categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='slug'
    )

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description',
            'price', 'brand', 'image',
            'categories',
            'time_added', 'time_updated'
        )


class CategorySerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField("get_preview_products")

    class Meta:
        model = Category
        fields = (
            'id', 'slug', 'name', 'description', 'products'
        )

    def get_preview_products(self, obj):
        result_set = obj.product_set.all()[:5]
        return ProductSerializer(result_set, many=True, read_only=True).data
