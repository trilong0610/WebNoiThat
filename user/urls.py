from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [
    path('accountDetail/', views.accountDetail, name = 'accountDetail' ),
    # Thay doi thong tin user
    path('changeInfoUser/', views.changeInfoUser, name="changeInfoUser"),
    path('login/', views.Login, name = 'login' ),
    path('logout/', views.LogoutUser, name = 'logout' ),
    path('register/', views.RegisterPage, name = 'register' ),
    path('ajax/load_district/', views.load_district, name='ajax_load_district'),
    path('ajax/load_wards/', views.load_wards, name='ajax_load_wards'),
    path('ajax/check_user_exist/', views.check_user_exist, name='ajax_check_user_exist'),
    path('ajax/check_email_exist/', views.check_email_exist, name='ajax_check_email_exist'),
    path('ajax/check_account_login/', views.check_account_login, name='ajax_check_account_login'),
]