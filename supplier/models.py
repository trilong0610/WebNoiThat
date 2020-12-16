from django.db import models

# Create your models here.
# Nha Cung Cap
class Supplier(models.Model):
    name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=11, default='')
    address = models.CharField(max_length=255, default='', null=True)
    def __str__(self):
        return self.name