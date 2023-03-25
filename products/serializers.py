from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description',
            'price', 'brand', 'image',
            'time_added', 'time_updated'
        )
