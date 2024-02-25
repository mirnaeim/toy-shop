from django.urls import path, include
from rest_framework import routers

from .views import add_to_cart, CartViewSet

cart_router = routers.DefaultRouter()
cart_router.register('', CartViewSet,)


urlpatterns = [
    path('add/<int:product_id>/<int:quantity>/', add_to_cart),
    path('carts/', include(cart_router.urls)),
]
