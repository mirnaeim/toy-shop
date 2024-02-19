from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Post, Comment
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'description',
            'category',
        )


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'post',
            'content',
            'created_date',
            'updated_date',
        )


class PostRetrieveSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'description',
            'comments',
            'category',
            'author',
        )



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token

