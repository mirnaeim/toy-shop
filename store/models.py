from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class MyBaseModel(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='Is active',)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date',)
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date',)

    class Meta:
        abstract = True
        ordering = ('pk',)

    def __str__(self):
        raise NotImplementedError('Implement __str__ method')


class Category(MyBaseModel):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='Title')
    description = models.TextField(null=False, blank=False, verbose_name='Description')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Product(MyBaseModel):
    name = models.CharField(max_length=250, null=False, blank=False, verbose_name='Name')
    detail = models.TextField(null=False, blank=False, verbose_name='Detail')
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.PROTECT,
                                 related_name='products', verbose_name='Category')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('id',)

    def __str__(self):
        return self.name

    @property
    def price(self):
        return self.prices.filter(is_active=True).last()


class Comment(MyBaseModel):
    # Just because of a conflict on User.comments on two blog and store apps we are forced to use another related_name
    # that is 'remarks', for author field in store.blog model
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='remarks',
                               verbose_name='Author')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='comments',
                                verbose_name='Products')
    content = models.TextField(null=False, blank=False, verbose_name='Content')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created_date',)

    def __str__(self):
        return f'{self.content} Commented by {self.author.username}'


class Price(MyBaseModel):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE,
                                related_name='prices', verbose_name='Product')
    value = models.PositiveBigIntegerField(null=False, blank=False, verbose_name='Value')
