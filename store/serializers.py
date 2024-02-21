from rest_framework import serializers

from .models import Category, Product, Comment, Price


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'description',
            'created_date',
            'updated_date',
        )


class CommentSerializer(serializers.ModelSerializer):
    # TODO user or product serializers, to not include or include and with read_only
    class Meta:
        model = Comment
        fields = (
            'product',
            'content',
        )


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('id', 'product', 'value')


class ProductSerializer(serializers.ModelSerializer):
    prices = PriceSerializer()  # Allow prices to be provided

    class Meta:
        model = Product
        fields = ('id', 'name', 'detail', 'category', 'prices')  # Add more fields if needed

    def create(self, validated_data):
        price = validated_data.pop('prices')
        product = Product.objects.create(**validated_data)
        Price.objects.create(product=product, **price)
        return product
