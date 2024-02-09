from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article_objects(models.Manager):

    def get_queryset(self):
        return super(Article_objects, self).get_queryset().filter(is_published=True)

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateField()
    category = models.ManyToManyField(Category)
    witer = models.ForeignKey(User, on_delete=models.CASCADE)
    myfiles = models.BinaryField(null=True)
    objects = models.Manager()
    objects_manager = Article_objects()
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='blog_images',null=True, blank=True)
    def __str__(self):
        return self.title


class Testi(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return self.title