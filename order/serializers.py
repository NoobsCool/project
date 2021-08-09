from rest_framework import serializers
from agent.models import Customer
from order.models import Order, Order_unit
from django.contrib.auth.models import User


class OrderUnitSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=False)

    class Meta:
        model = Order_unit
        fields = ['order', 'product', 'amount', 'price']


class OrderSerializer(serializers.ModelSerializer):
    orderunits = OrderUnitSerializer(many=True)
    customer = serializers.SlugRelatedField(slug_field='first_name', many=False, queryset=Customer.objects.all())
    creator = serializers.SlugRelatedField(slug_field='username', many=False, queryset=User.objects.all())

    class Meta:
        model = Order
        fields = [
            'id',
            'orderunits',
            'code',
            'code_year',
            'date_registered',
            'customer',
            'creator'
        ]

    def create(self, validated_data):
        orderunits_data = validated_data.pop('orderunits')
        order = Order.objects.create(**validated_data)
        for orderunit_data in orderunits_data:
            Order_unit.objects.create(order=order, **orderunit_data)
        return order

    def update(self, instance, validated_data):
        orderunits_data = validated_data.pop('orderunits')
        order = super(OrderSerializer, self).update(instance, validated_data)
        order.orderunits.all().delete()
        for orderunit_data in orderunits_data:
            Order_unit.objects.create(order=order, **orderunit_data)
        return order
