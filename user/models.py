from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
# class Account(AbstractUser):
#     sex_choice = ((0, "Nu"), (1, "Nam"), (2, "Khac"))
#     position_choice = (
#         (0, "admin"),
#         (1, "Quản lí"),
#         (2, "Nhân viên"),
#         (3, "Khách hàng"),
#     )
#     position = models.IntegerField(choices=position_choice, default=3)
#     age = models.IntegerField(default=0)
#     sex = models.IntegerField(choices=sex_choice, default=1)

    # tỉnh

class Province(models.Model):
    name = models.CharField(max_length = 50, default='')

    def __str__(self):
        return self.name

    # huyện
class District(models.Model):
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length = 50, default='')

    def __str__(self):
        return self.name

    # xã

class Wards(models.Model):
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length = 50, default='')

    def __str__(self):
        return self.name


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # tỉnh
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    # huyện
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    # xã
    wards = models.ForeignKey(Wards, on_delete=models.SET_NULL, null=True)
    # số nhà, tên đường
    address =  models.TextField(max_length=50, default='')

    phone = models.CharField(max_length=12, default='')

    def __str__(self):
        return self.user.username