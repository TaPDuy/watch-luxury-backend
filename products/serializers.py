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

    class Meta:
        model = Category
        fields = (
            'id', 'slug', 'name', 'description'
        )
