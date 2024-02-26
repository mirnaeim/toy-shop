from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Payment
from .serializers import PaymentSerializer
from cart.models import Cart


class PaymentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


@api_view()
@permission_classes((permissions.IsAuthenticated,))
def pay(request):
    customer = request.user
    cart_queryset = Cart.objects.filter(customer=customer, is_paid=False)
    if cart_queryset:
        cart = cart_queryset.first()
        cart.is_paid = True
        cart.save()
        payment = Payment.objects.create(
            customer=customer,
            cart=cart,
        )
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)
    else:
        return Response({"message": "No active cart for this user!"})


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})
