from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions

from .models import Cart, OrderItem
from store.models import Product
from .serializers import CartSerializer


class CartViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A ViewSet for viewing cart instances.
    """
    serializer_class = CartSerializer

    def get_queryset(self):
        customer = self.request.user
        return Cart.objects.filter(customer=customer, is_paid=False)


@api_view()
@permission_classes((permissions.IsAuthenticated,))
def add_to_cart(request, product_id, quantity):
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, id=product_id)
    customer = request.user

    cart = check_cart(customer)

    # Item already exists so quantity must update
    if cart.order_items.filter(product=product):
        order_item = get_object_or_404(cart.order_items, product=product)
        old_quantity = order_item.quantity
        order_item.quantity = old_quantity + quantity
        order_item.save()
    else:
        OrderItem.objects.create(
            cart=cart,
            product=product,
            price=product.price,
            quantity=quantity
        )
    serializer = CartSerializer(cart)
    return Response(serializer.data)


def check_cart(customer):
    cart = Cart.objects.filter(customer=customer, is_paid=False).first()
    if cart:
        print("Has Cart")
    else:
        print("New cart created")
        cart = Cart.objects.create(
            customer=customer,
        )
    return cart
