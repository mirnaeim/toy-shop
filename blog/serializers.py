from rest_framework import serializers

from blog.models import Category, Post, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'description',
        )


class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'category',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'content',
            'created_date',
            'updated_date',
        )


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'description',
            'comments',
            'category',
        )
