from django.db import models
from django.utils import timezone
from product.models import Product
from django.contrib.auth.models import User
from supplier.models import Supplier
# Create your models here.
# Don Nhap hang tu nha cung cap

class PurchaseProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # So luong san pham se nhap
    amount = models.IntegerField(default=0)
    time_create = models.DateTimeField(default=timezone.datetime.now())
    complete = models.BooleanField(default=False)
    def __str__(self):
        return self.product.title