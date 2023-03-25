from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from watchLuxuryAPI.utils import response_code as rescode

from .models import Product
from .serializers import ProductSerializer


class ProductView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, id):
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product)
        return Response({
            'code': rescode.API_SUCCESS,
            'msg': f'Retrived product',
            'data': serializer.data
        }, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes([IsAuthenticatedOrReadOnly, ])
def get_products(request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
            'code': rescode.API_SUCCESS,
            'msg': f'Retrived {len(products)} product(s)',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
