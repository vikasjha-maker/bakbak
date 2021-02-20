from django.db import models
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()

    def __str__(self):

        return f"{self.email}"


class Insta(models.Model):
    id = models.AutoField
    user_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='accounts/images', default="")

    def __str__(self):

        return self.user_name