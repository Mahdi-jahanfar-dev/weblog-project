import datetime
from time import timezone

from django.db import models
from django.contrib.auth.models import User
from django.db.models import OneToOneField
from django.contrib.auth.models import User
class Profile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    national_code = models.CharField(max_length=10)
    father_name = models.CharField(max_length=50)
    image = models.FileField(null=True, blank=True)

    class Meta:
        #for changing the name of this class in django admin panel we using this blow codes
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'


    def __str__(self):
        return self.user.username