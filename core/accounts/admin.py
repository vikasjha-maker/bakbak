from django.contrib import admin
from django.contrib.auth.models import User
from . models import CustomUser, Insta
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Insta)