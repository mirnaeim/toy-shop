from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet

category_router = routers.DefaultRouter()
category_router.register('', CategoryViewSet,)

product_router = routers.DefaultRouter()
product_router.register('', ProductViewSet,)


urlpatterns = [
    path('categories/', include(category_router.urls)),
    path('products/', include(product_router.urls)),
]

