from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from watchLuxuryAPI.utils import response_code as rescode
from users.models import User
from users.serializers import UserSerializer
from products.models import Product
from products.serializers import ProductSerializer

from .serializers import FavoriteSerializer
from .models import Favorite


@api_view(['GET', ])
@permission_classes([IsAuthenticatedOrReadOnly, ])
def get_user_favorite_products(request, id):
    try:
        user = User.objects.get(pk=id)
    except ObjectDoesNotExist:
        return Response({
            'code': rescode.API_NOT_FOUND,
            'msg': "User doesn't exist",
        }, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = ProductSerializer(user.favorites, many=True)
    return Response({
        'code': rescode.API_SUCCESS,
        'msg': f'Retrived {len(serializer.data)} product(s)',
        'data': serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes([IsAuthenticatedOrReadOnly, ])
def get_product_favorited_users(request, id):
    try:
        product = Product.objects.get(pk=id)
    except ObjectDoesNotExist:
        return Response({
            'code': rescode.API_NOT_FOUND,
            'msg': "Product doesn't exist",
        }, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(product.favorited_by, many=True)
    return Response({
        'code': rescode.API_SUCCESS,
        'msg': f'Retrived {len(serializer.data)} user(s)',
        'data': serializer.data
    }, status=status.HTTP_200_OK)


class FavoriteView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request):
        favorites = self.get_queryset()
        serializer = FavoriteSerializer(favorites, many=True)
        return Response({
            'code': rescode.API_SUCCESS,
            'msg': f'Retrived {len(favorites)} favorite(s)',
            'data': serializer.data
        }, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = FavoriteSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError:
                return Response({
                        'code': rescode.API_GENERIC_ERROR,
                        'msg': "Already favorited",
                    }, status=status.HTTP_400_BAD_REQUEST)
            return Response({
                'code': rescode.API_SUCCESS,
                'msg': 'Added to favorite',
                'data': serializer.data,
            }, status=status.HTTP_201_CREATED)
        else:
            error = [serializer.errors[error][0] for error in serializer.errors][0]
            match error.code:
                case 'does_not_exist':
                    return Response({
                        'code': rescode.API_NOT_FOUND,
                        'msg': "Provided user or product not found",
                    }, status=status.HTTP_400_BAD_REQUEST)
                case 'unique':
                    return Response({
                        'code': rescode.API_GENERIC_ERROR,
                        'msg': "Already favorited",
                    }, status=status.HTTP_400_BAD_REQUEST)
                case _:
                    return Response({
                        'code': rescode.API_GENERIC_ERROR,
                        'msg': "Couldn't add to favorite",
                    }, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):

        try:
            user = User.objects.get(pk=request.data.get('user'))
            product = Product.objects.get(pk=request.data.get('product'))
        except ObjectDoesNotExist:
            return Response({
                'code': rescode.API_NOT_FOUND,
                'msg': "Provided user or product not found",
            }, status=status.HTTP_400_BAD_REQUEST)

        query = Favorite.objects.filter(user=user, product=product)

        if query.count() > 0:
            query.delete()
            return Response({
                'code': rescode.API_SUCCESS,
                'msg': 'Removed favorite',
                'data': request.data,
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'code': rescode.API_GENERIC_ERROR,
                'msg': "Already removed",
            }, status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        queryset = Favorite.objects.all()
        user_id = self.request.query_params.get('user')
        product_id = self.request.query_params.get('product')

        if user_id:
            queryset = queryset.filter(user=user_id)
        if product_id:
            queryset = queryset.filter(product=product_id)

        return queryset

