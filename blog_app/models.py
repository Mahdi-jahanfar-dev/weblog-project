import datetime
from audioop import reverse

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    #we use verbose name for all field to change the variable name in django admin panel
    name = models.CharField(max_length=50, verbose_name='نام')
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.name)
        super(Category, self).save()

    def get_absolute_url(self):
        return reverse('blog_app:category_details', kwargs={'slug': self.slug})

    class Meta:
        #for changing the name of this class in django admin panel we using this blow codes
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
class Article_objects(models.Manager):
    def get_queryset(self):
        return super(Article_objects, self).get_queryset().filter(is_published=True)

class Article(models.Model):
    #we use verbose name for all field to change the variable name in django admin panel
    title = models.CharField(max_length=50, verbose_name='عنوان')
    content = models.TextField(verbose_name='توضیحات')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    category = models.ManyToManyField(Category, related_name='article', verbose_name='دسته بندی')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    myfiles = models.BinaryField(null=True)
    objects = models.Manager()
    objects_manager = Article_objects()
    is_published = models.BooleanField(default=True, verbose_name='وضعیت انتشار')
    image = models.ImageField(upload_to='blog_images', null=True, blank=True, verbose_name='عکس')
    slug = models.SlugField(null=True, unique=True, blank=True, verbose_name='اسلاگ')
    updated = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.title

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog_app:details', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-pub_date']
        #for changing the name of this class in django admin panel we using this blow codes
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"


class Comment(models.Model):
    #we use verbose name for all field to change the variable name in django admin panel
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله')
    content = models.TextField(verbose_name='محتوا')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='کاربر')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', null=True, blank=True, verbose_name='والد')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')


    def __str__(self):
        return self.content[:10]

    class Meta:
        #for changing the name of this class in django admin panel we using this blow codes
        verbose_name = "نطر"
        verbose_name_plural = "نطرات"


class Contactus(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        #for changing the name of this class in django admin panel we using this blow codes
        #it for mofrad
        verbose_name = "ارتباط با ما"
        #we using this for gam
        verbose_name_plural = "ارتباطات"