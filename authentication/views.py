import jwt

from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from watchLuxuryAPI.settings import SECRET_KEY, SIMPLE_JWT
from watchLuxuryAPI.utils import response_code as rescode

from .serializers import (
    UserSerializer, LoginSerializer, 
    UserUpdateSerializer, ChangePasswordSerializer
)
from .models import User
from .utils import EmailUtil


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({
                'code': rescode.API_INVALID_LOGIN,
                'msg': 'Invalid login info',
            }, status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            'code': rescode.API_SUCCESS,
            'msg': 'User authenticated',
            'data': serializer.validated_data,
        }, status=status.HTTP_200_OK)


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

            return Response({
                'code': rescode.API_SUCCESS,
                'msg': f'Created user',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'code': rescode.API_GENERIC_ERROR,
                'msg': 'Request failed',
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


@api_view(['GET', ])
@permission_classes([IsAdminUser, ])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({
        'code': rescode.API_SUCCESS,
        'msg': f'Retrived {len(users)} user(s)',
        'data': serializer.data
    }, status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, id):
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user)
        return Response({
            'code': rescode.API_SUCCESS,
            'msg': f'Retrived user',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        print(request.data)

        user = User.objects.get(pk=id)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': rescode.API_SUCCESS,
                'msg': f'Updated user',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        
        print(serializer.errors)
        return Response({
            'code': rescode.API_GENERIC_ERROR,
            'msg': 'Request failed',
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
@permission_classes([IsAuthenticated, ])
def change_password(request, id):
    print(request.data)

    user = User.objects.get(pk=id)
    serializer = ChangePasswordSerializer(user, data=request.data)
    if serializer.is_valid():
        if not user.check_password(serializer.validated_data['old_password']):
            return Response({
                'code': rescode.API_WRONG_PASSWORD,
                'msg': 'Wrong password',
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({
            'code': rescode.API_SUCCESS,
            'msg': 'Password updated'
        }, status=status.HTTP_200_OK)
    
    print(serializer.errors)
    return Response({
        'code': rescode.API_GENERIC_ERROR,
        'msg': 'Request failed',
    }, status=status.HTTP_400_BAD_REQUEST)
