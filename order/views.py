import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from cart.models import Cart,CartItem
# Create your views here.
from order.models import Order
from datetime import datetime

from product.models import Category, Product


class recentOrder(View):
    def get(self, request):
        user = request.user
        orders = Order.objects.filter(user_id=user.id).order_by('-date_ordered')
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
        context = {'orders': orders,
                   'category': category,
                   'cartItems': cartItems
                   }
        return render(request, 'order/RecentOrder.html', context)


def addOrder(request, cart_id):
    user = request.user
    cart = cart_id
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    email = request.POST['email']
    phone = request.POST['phone']
    province = request.POST['province']
    district = request.POST['district']
    wards = request.POST['wards']
    address = request.POST['address']


    order, created = Order.objects.get_or_create(user = user, cart_id = cart)

    order.fistName = firstName
    order.lastName = lastName
    order.email = email
    order.phone = phone
    order.province = province
    order.district = district
    order.wards = wards
    order.address = address
    order.date_ordered = datetime.now()
    order.transaction_id = cart
    order.save()
    updateCart = Cart.objects.get(id = cart)
    updateCart.complete = True
    # cap nhat so luong da ban va ton kho cua san pham
    cart = Cart.objects.get(id = cart_id)
    for item in cart.cartitem_set.all():
        product = Product.objects.get(id = item.product.id)
        product.amount = product.amount - item.quantity
        product.amount_sell = product.amount_sell + item.quantity
        product.save()

    updateCart.save()
    context = {'cart_id':cart_id}
    return render(request,'order/OrderComplete.html', context)