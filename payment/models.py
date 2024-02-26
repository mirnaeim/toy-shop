from django.db import models
from django.contrib.auth.models import User

from cart.models import Cart

# Create your models here.


class Payment(models.Model):
    customer = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT, related_name='payments',
                                 verbose_name='Customer')
    cart = models.ForeignKey(Cart, null=False, blank=False, on_delete=models.PROTECT, related_name='payments',
                             verbose_name='Cart')
    transaction_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date',)


