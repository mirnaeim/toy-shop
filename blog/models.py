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


class Post(MyBaseModel):
    title = models.CharField(max_length=250, null=False, blank=False, verbose_name='Title')
    description = models.TextField(null=False, blank=False, verbose_name='Description')
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.PROTECT,
                                 related_name='posts', verbose_name='Category')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Comment(MyBaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(verbose_name='Content')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created_date',)

    def __str__(self):
        return f'Comment by {self.created_date}'