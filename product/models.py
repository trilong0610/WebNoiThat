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
    amount = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    date_add = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
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
