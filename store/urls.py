from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet, PriceViewSet, ReviewViewSet

category_router = routers.DefaultRouter()
category_router.register('', CategoryViewSet,)

product_router = routers.DefaultRouter()
product_router.register('', ProductViewSet,)

price_router = routers.DefaultRouter()
price_router.register('', PriceViewSet, )

review_router = routers.DefaultRouter()
review_router.register('', ReviewViewSet)

urlpatterns = [
    path('categories/', include(category_router.urls)),
    path('products/', include(product_router.urls)),
    path('prices/', include(price_router.urls)),
    path('reviews/', include(review_router.urls)),
]
