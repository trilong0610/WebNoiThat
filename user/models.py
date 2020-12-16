from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.
# class MyUser(AbstractUser):
#     sex_choice = ((0, "Nu"), (1, "Nam"), (2, "Khac"))
#     age = models.IntegerField(default=0)
#     sex = models.IntegerField(choices=sex_choice, default=0)
#     address = models.CharField(default='', max_length= 255)