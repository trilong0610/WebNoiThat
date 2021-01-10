from django.contrib import admin
from .models import Province,District,Wards,Address
# Register your models here.
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Wards)
admin.site.register(Address)