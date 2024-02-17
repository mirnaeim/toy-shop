from rest_framework import viewsets, filters
# from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Category
from .serializers import CategorySerializer, ProductSerializer
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('pk')

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('-pk')

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ('id', 'category',)
    search_fields = ('title', 'description',)

# Create your views here.
