from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView

from watchLuxuryAPI.utils import response_code as rescode

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .filters import SearchFilter


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


class ProductsView(GenericAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = (SearchFilter, )
    search_fields = ('name', 'brand', )

    def get(self, request):
        products = self.filter_queryset(self.get_queryset())
        serializer = ProductSerializer(products, many=True)
        return Response({
            'code': rescode.API_SUCCESS,
            'msg': f'Retrived {len(products)} product(s)',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = Product.objects.all()
        category_slug = self.request.query_params.get('category')

        if category_slug:
            try:
                category = Category.objects.get(slug=category_slug)
            except ObjectDoesNotExist:
                return queryset.none()
            queryset = category.product_set.all()

        return queryset


@api_view(['GET', ])
@permission_classes([IsAuthenticatedOrReadOnly, ])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response({
        'code': rescode.API_SUCCESS,
        'msg': f'Retrived {len(categories)} category(s)',
        'data': serializer.data
    }, status=status.HTTP_200_OK)
