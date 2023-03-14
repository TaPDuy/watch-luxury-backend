import jwt

from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from watchLuxuryAPI.settings import SECRET_KEY, SIMPLE_JWT
from .serializers import UserSerializer, LoginSerializer, UserUpdateSerializer
from .models import User
from .utils import EmailUtil


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny, )

    serializer_class = LoginSerializer


class RegisterView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relative_link = reverse('verify_email')
            EmailUtil.send_email(
                'Verify your email',
                f"""Hi {user.username}. Use the link below to verify your email \n
                http://{current_site}{relative_link}?token={str(token)}
                """,
                user.email
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error_msg': 'Something went wrong!'
            }, status=status.HTTP_400_BAD_REQUEST)
        


class VerifyEmailView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        token = request.query_params.get('token')

        if not token:
            return Response({"msg": "Please provide an access token"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            payload = jwt.decode(token, SECRET_KEY, [SIMPLE_JWT["ALGORITHM"]])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
            return Response({"msg": "User account successfully activated!"}, status=status.HTTP_200_OK)
        except jwt.exceptions.ExpiredSignatureError:
            return Response({"msg": "Activation link expired."}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.InvalidSignatureError:
            return Response({"msg": "Invalid activation link."}, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, id):
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        print(request.data)

        user = User.objects.get(pk=id)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
        
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
