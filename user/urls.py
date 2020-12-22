from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [
    path('accountDetail/', views.accountDetail, name = 'accountDetail' ),
    path('login/', views.LoginPage, name = 'login' ),
    path('logout/', views.LogoutUser, name = 'logout' ),
]