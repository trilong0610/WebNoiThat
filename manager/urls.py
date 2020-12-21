from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
app_name = 'manager'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('purchase_product/', views.purchase_product.as_view(), name = 'purchase_product'),
    # quan li them xoa sua hang hoa
    path('add_category/', views.add_category.as_view(), name = "add_category"),
    path('add_product/', views.add_product.as_view(), name = "add_product"),
    # Phan quyen
    path('view_user/', views.view_User.as_view(), name = "view_user"),
    path('gains_permission/<int:user_id>', views.gains_permission.as_view(), name = "view_permission"),
    path('gains_permission/', views.updatePermission, name = "gains_permission"),
    path('view_shipping/', views.view_shipping.as_view(), name = 'view_shipping'),
    path('update_shipping/', views.updateShipping, name = 'update_shipping'),

    #them, xoa, sua sp
    path('dashboad/', views.dashboard, name="dashboard"),
    path('edit/<int:id>', views.edit, name = 'edit_product'),
    path('update/<int:id>', views.update, name = 'update_product'),
    path('delete/<int:id>', views.destroy, name = 'delete_product'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)