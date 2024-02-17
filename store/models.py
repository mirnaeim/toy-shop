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
    price = models.CharField(max_length=255, null=False, blank=False, verbose_name='price')
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.PROTECT,
                                 related_name='posts', verbose_name='Category')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('id',)

    def __str__(self):
        return self.name
