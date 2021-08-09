import datetime

import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from agent.serializers import CustomerSerializer, UserReadSerializer
from agent.models import Customer
from django.contrib.auth.models import User
from rest_framework import status


# Create your views here.

class CustomerListCreateAPIView(ListCreateAPIView):
    queryset = Customer.objects.filter(deleted=False)
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]

    def get_paginated_response(self, data):
        return Response(data)


class CustomerGetAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CustomerSerializer(instance)
        return Response(serializer.data)


class CustomerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        product.deleted = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserReadSerializer
    permission_classes = [AllowAny]

    def get_paginated_response(self, data):
        return Response(data)


class UserGetAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserReadSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserReadSerializer(instance)
        return Response(serializer.data)



class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserReadSerializer
    permission_classes = [AllowAny]

