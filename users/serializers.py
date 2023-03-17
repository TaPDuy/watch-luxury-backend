from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    def validate_password(self, password):
        return make_password(password)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'password',
            'first_name', 'last_name',
            'email', 'address', 'phone_number',
            'is_active', 'is_admin',
            'last_login', 'date_joined'
        )
        extra_kwargs = {'password': {'write_only': True}}


class UserUpdateSerializer(UserSerializer):

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name',
            'email', 'address', 'phone_number'
        )


class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
