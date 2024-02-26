from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Cart, OrderItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'product',
            'price',
            'quantity'
        )


class CartSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'is_paid',
            'get_total_cost',
            'customer',
            'order_items',
        )


