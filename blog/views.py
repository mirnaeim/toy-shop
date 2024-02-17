from rest_framework import viewsets, filters
# from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Post, Category, Comment
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, PostListSerializer
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('pk')

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_active=True).order_by('-pk')


    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ('id', 'category',)
    search_fields = ('title', 'description',)

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(is_active=True)

