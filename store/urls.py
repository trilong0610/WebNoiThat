from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
app_name = 'store'
urlpatterns = [
    # trang chu
    path('', views.home, name="home"),
    # gio hang
    path('productGrid/', views.view_product, name = 'productGrid'),
    # thanh toan
    path('updateItem/', views.updateItem, name="updateItem"),
    path('addItemToCart/', views.addItemToCart, name="addItemToCart"),

    path('contact/', views.contact, name="contact"),
    # xem san pham trong danh muc
    path('category/<int:category_id>/', views.view_category.as_view(), name = "category"),
    path('hotProduct/', views.hot_product, name="hotProduct"),
    path('mostPopular/', views.most_popular, name="mostPopular"),
    path('detailProduct/<int:product_id>', views.detailProduct, name="detailProduct"),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
