from django.contrib import admin
from .models import CartItem,ShippingAddress,Cart
# Register your models here.
admin.site.register(CartItem)
admin.site.register(ShippingAddress)
admin.site.register(Cart)