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
        return self.prices.filter(is_active=True).first().value

    def media(self):
        return self.product_media.filter(is_active=True).all()

    def images(self):
        return self.product_media.filter(is_active=True, media_type='image').all()

    def videos(self):
        return self.product_media.filter(is_active=True, media_type='video').all()

    def audios(self):
        return self.product_media.filter(is_active=True, media_type='audio').all()


class Price(MyBaseModel):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE,
                                related_name='prices', verbose_name='Product')
    value = models.PositiveBigIntegerField(blank=False, null=False, verbose_name='Value')

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'
        ordering = ('-created_date',)

    def __str__(self):
        return f'{self.value} $'


class Review(MyBaseModel):
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='reviews',
                               verbose_name='Author')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='reviews',
                                verbose_name='Products')
    content = models.TextField(null=False, blank=False, verbose_name='Content')

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'{self.content}'


class ProductMedia(MyBaseModel):
    MEDIA_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),

    )

    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE,
                                related_name='product_media', verbose_name='Products')
    media_type = models.CharField(max_length=6, choices=MEDIA_TYPE_CHOICES)
    media_file = models.FileField(upload_to='store/product/')

    def __str__(self):
        return self.product.name
