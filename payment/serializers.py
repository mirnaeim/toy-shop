from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Payment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class PaymentSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = (
            'customer',
            'cart'
        )
