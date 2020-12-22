from django.urls import path
from order import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
app_name = 'order'
urlpatterns = [
    # gio hang
    path('', views.cart, name="order"),
]