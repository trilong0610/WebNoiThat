from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from cart.models import Cart
from product.models import Product


class Order(models.Model):
    STATUS =(
        ('1', 'Đã tiếp nhận'),
        ('2', 'Đang chuẩn bị'),
        ('3', 'Đang giao hàng'),
        ('4', 'Đã giao hàng'),
        ('5', 'Đã hủy'),
        ('6', 'Tạm ngưng'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS, default='1')
    transaction_id = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user.username)

    #
    # @property
    # def get_cart_total(self):
    #     cartitem = self.cartitem.all()
    #     total = sum([item.get_total for item in cartitem])
    #     return total
    #
    # @property
    # def get_cart_items(self):
    #     cartitem = self.cartitem_set.all()
    #     total = sum([item.quantity for item in cartitem])
    #     return total
    #
    # @property
    # def shipping(self):
    #     shipping = False
    #     cartitem = self.cartitem_set.all()
    #     for i in cartitem:
    #         if i.product.digital == False:
    #             shipping = True
    #     return shipping

