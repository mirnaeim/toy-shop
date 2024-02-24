from rest_framework import viewsets, filters
# from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Category, Price, Review
from .serializers import CategorySerializer, ProductSerializer, PriceSerializer, ReviewSerializer
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


class PriceViewSet(viewsets.ModelViewSet):
    serializer_class = PriceSerializer
    queryset = Price.objects.all().order_by('-pk')


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.filter(is_active=True)

    def perform_create(self, serializer):
        # Assign the current user to the author field of the post
        serializer.save(author=self.request.user)
