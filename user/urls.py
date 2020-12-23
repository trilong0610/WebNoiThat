from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [
    path('accountDetail/', views.accountDetail, name = 'accountDetail' ),
    # Thay doi thong tin user
    path('changeInfoUser/', views.changeInfoUser, name="changeInfoUser"),
    path('recentOrder/', views.recentOrder, name='recentOrder'),
    path('login/', views.LoginPage, name = 'login' ),
    path('logout/', views.LogoutUser, name = 'logout' ),
]