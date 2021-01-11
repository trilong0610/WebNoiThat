from django.db import models
# Create your models here.
class Category(models.Model):
    title = models.CharField(default='',max_length=255)
    description = models.TextField(default='', blank=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(default='',max_length=255)
    price  = models.IntegerField(default=0)
    description = models.TextField(default='', blank=True)
    active = models.BooleanField(default=True)
    date_add = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    amount = models.IntegerField(default=0)
    amount_sell = models.IntegerField(default=0)
    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    @property
    def home_product(self):
        product = Product.objects.all()
        return product

    @property
    def total_amount_remain(self):
        size = self.sizeproduct_set.all()
        total = sum([item.amount for item in size])
        return total

    @property
    def total_amount_sell(self):
        size = self.sizeproduct_set.all()
        total = sum([item.amount_sell for item in size])
        return total

class SizeProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    horizontal = models.IntegerField(default=0)
    vertical = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.product.title

