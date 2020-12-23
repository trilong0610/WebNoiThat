import json

from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

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


def recentOrder(request):
    user = request.user
    orders = Order.objects.filter(user_id=user.id)
    context = {'orders':orders,
               }
    return render(request, 'user/RecentOrder.html', context)


def RegisterPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            messages.success(request,'Account was created for ' + user)
            return redirect('login')
    context = {'form': form}
    return  render(request, 'user/register.html', context)


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
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
    firstName = data['firstName']
    lastName = data['lastName']
    email = data['email']
    user.first_name = firstName
    user.last_name = lastName
    user.email = email
    user.save()
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
    address = Address.objects.get(user = user)
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



