from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
urlpatterns = [
    # trang chu
    path('', views.store, name="store"),
    # gio hang

    # thanh toan
    path('updateItem/', views.updateItem, name="updateItem"),
    # xem san pham trong danh muc
    path('category/<int:category_id>/', views.view_category.as_view(), name = "category"),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
