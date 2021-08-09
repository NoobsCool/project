from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from agent.models import Customer
from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'company_name', 'deleted']


class UserReadSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'email', 'username']
