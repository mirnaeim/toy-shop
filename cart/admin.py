from django.contrib import admin
from django.contrib.admin import register

from .models import Cart, OrderItem


@register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


