from django.urls import path
from . import views

urlpatterns = [
    path('',views.shipping_status, name = 'shipping_status')
]