import json

from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User

from django.contrib import messages

# Dic check login def
from django.contrib.auth import authenticate, login, decorators
# Dic check login class base view
from django.contrib.auth.mixins import LoginRequiredMixin

from cart.models import Cart
from order.models import Order
from product.models import Category
from .forms import  CreateUserForm
from django.http import HttpResponseRedirect

# def accountDetail(request):
#     if request.user.is_authenticated:
#         user = request.user
#         cart, created = Cart.objects.get_or_create(user=user, complete=False)
#         items = cart.cartitem_set.all()
#         cartItems = cart.get_cart_items
#     else:
#         items = []
#         cart = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
#         cartItems = cart['get_cart_items']
#     category = Category.objects.all()
#     context = {
#         'cartItems': cartItems,
#         'category':category,
#     }
#     return render(request, 'user/AccountDetail.html', context)
from .models import Address, District, Wards, Province


def RegisterPage(request):
    if request.method == 'POST':
        username = request.POST["user"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2 and password1 != '' and password2 != '':
            user = User.objects.create_user(username=username, email=email, password=password2)
        else:
            return render(request, 'user/MyAccount.html', {'error': 0})
        return render(request, 'user/RegisterSuccess.html', {'username': user.username})

def Login(request):
    if request.user.is_authenticated:
        return redirect('user:accountDetail')
    else:
        if request.method == 'POST':
            username = request.POST['user']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('store:home')
        context = {}
        return render(request, 'user/MyAccount.html', context)

def LogoutUser(request):
    logout(request)
    return redirect('/')

def changeInfoUser(request):
    if request.method == "POST":
        user = request.user
        user_address, created = Address.objects.get_or_create(user = user)

        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phone']
        province = Province.objects.get(id = request.POST['province'])
        district = District.objects.get(id = request.POST['district'])
        wards = Wards.objects.get(id = request.POST['wards'])
        address = request.POST['address']

        user.first_name = firstName
        user.last_name = lastName
        user.email = email
        user.save()

        user_address.phone = phone
        user_address.province = province
        user_address.district = district
        user_address.wards = wards
        user_address.address = address
        user_address.save()
        return redirect('user:accountDetail')


def accountDetail(request):
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, complete=False)
        items = cart.cartitem_set.all()
        cartItems = cart.get_cart_items
    else:
        items = []
        cart = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = cart['get_cart_items']
    category = Category.objects.all()
    province = Province.objects.all()
    address, created = Address.objects.get_or_create(user = user)
    context = {
        'province':province,
        'cartItems': cartItems,
        'category': category,
        'address': address,
    }
    return render(request, 'user/AccountDetail.html', context)

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user:accountDetail')
        else:
            messages.error(request, 'Sai thông tin, vui lòng nhập lại.')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'user/AccountDetail.html', context)


def load_district(request):
    province_id = request.GET.get('province')
    district = District.objects.filter(province_id=province_id).order_by('name')
    return render(request, 'user/district_dropdown_list_options.html', {'district': district})

def load_wards(request):
    district_id = request.GET.get('district')
    wards = Wards.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'user/ward_dropdown_list_options.html', {'wards': wards})

def check_user_exist(request):
    username = request.GET.get('username')
    data ={
        'is_taken': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)
def check_email_exist(request):
    email = request.GET.get('email')
    data ={
        'is_taken': User.objects.filter(email = email).exists()
    }
    return JsonResponse(data)

def check_account_login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        data = {
            'is_taken': "ok"
        }
    else:
        data = {
            'is_taken': ""
        }
    return JsonResponse(data)
