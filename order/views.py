from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from watchLuxuryAPI.utils import response_code as rescode

from .serializers import OrderReadonlySerializer, OrderWriteonlySerializer
from .models import Order


class OrderView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request):
        orders = self.get_queryset()
        serializer = OrderReadonlySerializer(orders, many=True)
        return Response({
            'code': rescode.API_SUCCESS,
            'msg': f'Retrived {len(serializer.data)} order(s)',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderWriteonlySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': rescode.API_SUCCESS,
                'msg': f'Created order',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response({
                'code': rescode.API_GENERIC_ERROR,
                'msg': f'Unable to order',
            }, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Order.objects.all()
        user_id = self.request.query_params.get('user')

        if user_id:
            queryset = queryset.filter(user=user_id)
        
        return queryset
