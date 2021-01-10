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
]