from django.contrib.auth.models import User
from django.db import models

from store.models import Product
# Create your models here.


class Cart(models.Model):
    customer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='cart',
                                 verbose_name='Customer')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=25)
    city = models.CharField(max_length=50)
    is_paid = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'Cart {self.id}'

    @property
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.order_items.all())


class OrderItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
