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
from .models import Address

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
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'user/MyAccount.html', context)

def LogoutUser(request):
    logout(request)
    return redirect('/')

def changeInfoUser(request):
    data = json.loads(request.body)
    user = request.user
    user_address, created = Address.objects.get_or_create(user = user)

    firstName = data['firstName']
    lastName = data['lastName']
    email = data['email']
    phone = data['phone']
    province = data['province']
    district = data['district']
    wards = data['wards']
    address = data['address']

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
    return JsonResponse('Info was change', safe=False)

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
    address, created = Address.objects.get_or_create(user = user)
    context = {
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



