from django.db import models
from product.models import Product, SizeProduct
from django.contrib.auth.models import User
from os import path
# Create your models here.

class Cart(models.Model):
    STATUS =(
        ('1', 'Đang chuẩn bị'),
        ('2', 'Đang vận chuyển'),
        ('3', 'Đã giao'),
        ('4', 'Tạm ngưng'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        cartitem = self.cartitem_set.all()
        total = sum([item.get_total for item in cartitem])
        return total

    @property
    def get_cart_items(self):
        cartitem = self.cartitem_set.all()
        total = sum([item.quantity for item in cartitem])
        return total




class CartItem(models.Model):
    sizeProduct = models.ForeignKey(SizeProduct, on_delete=models.SET_NULL,blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL,blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.cart.id)
    @property
    def get_total(self):
        total = self.sizeProduct.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user