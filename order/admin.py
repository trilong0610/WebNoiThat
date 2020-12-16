from django.contrib import admin
from .models import OrderItem,ShippingAddress,Order
# Register your models here.
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Order)