from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, LoginSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({ 'msg': 'Register successful', 'data': user}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({
                'error_msg': 'Something went wrong!'
            }, status=status.HTTP_400_BAD_REQUEST)
