from django.contrib.admin import register
from django.contrib import admin
from .models import Category, Post, Comment
# Register your models here.


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category')


@register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'post')
