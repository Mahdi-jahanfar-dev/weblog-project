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
    image = models.FileField()