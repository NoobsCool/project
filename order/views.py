from rest_framework import status
from rest_framework.generics import *
from rest_framework.permissions import (AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)
from rest_framework.response import Response

from order.serializers import *
from order.models import *


# Create your views here.

class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [AllowAny]

    def get_paginated_response(self, data):
        return Response(data)


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]


class OrderGetAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = OrderSerializer(instance)
        return Response(serializer.data)
