from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Order


class OrderReadonlySerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    total = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = (
            'id', 'user', 'name', 'phone_number', 'address',
            'products', 'total', 'status', 'time_added', 
        )
        read_only_fields = ('total', 'status', 'time_added', )
        depth = 1

    def get_user(self, obj):
        return UserSerializer(obj.user).data
    

class OrderWriteonlySerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('user', 'name', 'phone_number', 'address', 'products', )
