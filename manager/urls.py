from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
app_name = 'manager'
urlpatterns = [
    path('', views.home.as_view(), name = 'home'),
    path('purchase_product/', views.purchaseProduct.as_view(), name = 'purchase_product'),

    # quan li them xoa sua hang hoa
    path('add_category/', views.add_category.as_view(), name = "add_category"),
    path('add_product/', views.add_product.as_view(), name = "add_product"),

    # Phan quyen
    path('userControl/', views.view_User.as_view(), name = "view_user"),
    path('gainsPermission/<int:user_id>', views.gains_permission.as_view(), name = "view_permission"),
    path('gainsPermission/', views.updatePermission, name = "gains_permission"),
    path('viewShipping/', views.view_shipping.as_view(), name = 'view_shipping'),
    path('updateShipping/', views.updateShipping, name = 'update_shipping'),

    #them, xoa, sua sp
    path('productControl/', views.productControl, name="product_control"),
    path('editProduct/<int:product_id>', views.editProduct.as_view(), name = 'edit_product'),
    path('test/', views.test, name="test"),
    path('register/', views.register, name="register"),
    path('sizeProductControl/<int:product_id>', views.sizeProductControl.as_view(), name="sizeProductControl"),
    path('addSizeProduct/<int:product_id>', views.addSizeProduct.as_view(), name="addSizeProduct"),
    path('ajax/validate_size', views.validate_size, name="validate_size"),

    #them, xoa, sua user
    path('register/', views.register, name="register"),
    path('editUser/<int:user_id>', views.editUser.as_view(), name="editUser"),
    path('deleteUser/<int:user_id>', views.destroyUser, name = 'delete_user'),

    #them, xoa, sua don nhap san pham
    path('purchaseControl/', views.viewPurchaseProduct, name="viewPurchase"),
    path('deletePurchase/<int:purchase_id>', views.destroyPurchase, name = 'delete_purchase'),
    path('editPurchase/<int:purchase_id>', views.editPurchase.as_view(), name="editPurchase"),
    path('ajax/load_sizeProduct/', views.load_sizeProduct, name='ajax_load_wards'),

    # Order
    path('orderControl/', views.orderControl.as_view(), name="orderControl"),
    path('editOrder/<int:order_id>', views.editOrder.as_view(), name="editOrder"),

#     danh mucj
    path('categoryControl/', views.categoryControl, name="categoryControl"),
    path('addCategory/', views.addCategory.as_view(), name="addCategory"),
    path('editCategory/<int:category_id>', views.editCategory.as_view(), name="editCategory"),
#   doanh thu
    path('revenue/', views.revenue.as_view(), name="revenue"),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)