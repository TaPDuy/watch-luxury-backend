from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from watchLuxuryAPI.utils import response_code as rescode

from .models import User
from .serializers import UserSerializer, ChangePasswordSerializer, UserUpdateSerializer


class UserView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

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


@api_view(['GET', ])
@permission_classes([IsAuthenticatedOrReadOnly, ])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({
        'code': rescode.API_SUCCESS,
        'msg': f'Retrived {len(users)} user(s)',
        'data': serializer.data
    }, status=status.HTTP_200_OK)


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
