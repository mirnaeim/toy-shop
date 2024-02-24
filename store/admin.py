from django.contrib import admin
from django.contrib.admin import register
from .models import Product, Category, Price, Review, ProductMedia
# Register your models here.


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'detail', 'category')


@register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'value')


@register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('content', 'author')


@register(ProductMedia)
class PostMediaAdmin(admin.ModelAdmin):
    list_display = ('get_media_type_display',)
