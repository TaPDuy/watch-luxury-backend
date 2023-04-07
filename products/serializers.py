from rest_framework import serializers

from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):

    categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='slug'
    )
    favorites = serializers.SerializerMethodField("get_favorites_count")

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description',
            'price', 'brand', 'image',
            'favorites',
            'categories',
            'time_added', 'time_updated'
        )

    def get_favorites_count(self, obj):
        return obj.favorite_set.count() 


class CategorySerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField("get_preview_products")

    class Meta:
        model = Category
        fields = (
            'id', 'slug', 'name', 'description', 'products'
        )

    def get_preview_products(self, obj):
        result_set = obj.product_set.all().order_by('-price')[:7]
        return ProductSerializer(result_set, many=True, read_only=True).data
