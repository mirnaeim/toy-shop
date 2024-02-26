from django.urls import path, include
from rest_framework import routers

from .views import PaymentViewSet, pay

payment_router = routers.DefaultRouter()
payment_router.register('', PaymentViewSet)


urlpatterns = [
    # path('add/<int:product_id>/<int:quantity>/', add_to_cart),
    path('pay/', pay),
    path('', include(payment_router.urls)),
]
