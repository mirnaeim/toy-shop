from django.db import models
from django.contrib.auth.models import User

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
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='Title')
    description = models.TextField(null=False, blank=False, verbose_name='Description')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Post(MyBaseModel):
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=False, blank=False, verbose_name='Title')
    description = models.TextField(null=False, blank=False, verbose_name='Description')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='posts', verbose_name='Category')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('id',)

    def __str__(self):
        return self.title

    def media(self):
        return self.post_media.filter(is_active=True).all()

    def images(self):
        return self.post_media.filter(is_active=True, media_type='image').all()

    def videos(self):
        return self.post_media.filter(is_active=True, media_type='video').all()

    def audios(self):
        return self.post_media.filter(is_active=True, media_type='audio').all()



class Comment(MyBaseModel):
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='comments',
                               verbose_name='Author')
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE, related_name='comments',
                             verbose_name='Post')
    content = models.TextField(null=False, blank=False, verbose_name='Content')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created_date',)

    def __str__(self):
        return f'{self.content} Commented by {self.author.username}'


class PostMedia(MyBaseModel):
    MEDIA_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),

    )

    product = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE,
                                related_name='post_media', verbose_name='Posts')
    media_type = models.CharField(max_length=6, choices=MEDIA_TYPE_CHOICES)
    media_file = models.FileField(upload_to='blog/post/')

    def __str__(self):
        return self.product.title
