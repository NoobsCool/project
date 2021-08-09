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

class LoginView(APIView):
    def post(self,request):
        username=request.data['username']
        password=request.data['password']

        user=User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload={
            'id':user.id,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }

        token = jwt.encode(payload,'secret',algorithm='HS256').decode('utf-8')

        return Response({
            'jwt':token
        })