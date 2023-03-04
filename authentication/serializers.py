from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'password',
            'first_name', 'last_name',
            'email', 'address', 'phone_number',
            'is_active', 'is_admin',
            'last_login', 'date_joined'
        )
        extra_kwargs = {'password': {'write_only': True}}
