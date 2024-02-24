from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Category, Product, Price, Review, ProductMedia


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'description',
        )


class ReviewSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = (
            'id',
            'author',
            'product',
            'content',
        )


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = (
            'value',
        )


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMedia
        fields = (
            'id',
            'media_type',
            'media_file',
        )


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    media = MediaSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'name',
            'detail',
            'price',
            'reviews',
            'media',
            )
