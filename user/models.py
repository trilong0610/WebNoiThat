from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
# class MyUser(AbstractUser):
#     sex_choice = ((0, "Nu"), (1, "Nam"), (2, "Khac"))
#     age = models.IntegerField(default=0)
#     sex = models.IntegerField(choices=sex_choice, default=0)
#     address = models.CharField(default='', max_length= 255)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # tỉnh
    province = models.TextField(max_length=50, default='')
    # huyện
    district = models.TextField(max_length=50, default='')
    # xã
    wards = models.TextField(max_length=50, default='')
    # số nhà, tên đường
    address =  models.TextField(max_length=50, default='')
    phone = models.CharField(max_length=12, default='')