from audioop import reverse

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    def __str__(self):
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.name)
        super(Category, self).save()

    def get_absolute_url(self):
        return reverse('blog_app:category_details', kwargs={'slug': self.slug})
class Article_objects(models.Manager):
    def get_queryset(self):
        return super(Article_objects, self).get_queryset().filter(is_published=True)

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, related_name='article')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    myfiles = models.BinaryField(null=True)
    objects = models.Manager()
    objects_manager = Article_objects()
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='blog_images', null=True, blank=True)
    slug = models.SlugField(null=True, unique=True, blank=True)
    def __str__(self):
        return self.title

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog_app:details', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content[:10]