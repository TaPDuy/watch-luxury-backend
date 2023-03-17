import jwt

from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from watchLuxuryAPI.settings import SECRET_KEY, SIMPLE_JWT
from watchLuxuryAPI.utils import response_code as rescode

from users.serializers import UserSerializer
from users.models import User

from .serializers import LoginSerializer
from .utils import EmailUtil


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid()
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
        if serializer.is_valid():
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
