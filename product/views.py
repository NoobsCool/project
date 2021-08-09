from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from product.serializers import ProductSerializer
from product.models import Product
from rest_framework import status


# Create your views here.
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.filter(deleted=False)
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_paginated_response(self, data):
        return Response(data)


class ProductGetAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductSerializer(instance)
        return Response(serializer.data)


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        product.deleted = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
