import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

from cart.models import Cart,CartItem
# Create your views here.
from order.models import Order
from datetime import datetime

def cart(request):
    if request.user.is_authenticated:
        customer = User.objects.get(pk = request.user.id)
        cart, created = Cart.objects.get_or_create( user = request.user, complete=False)
        # carts = Order.objects.get(pk = customer)
        items = cart.orderitem_set.all()
        cartItems = cart.get_cart_items
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0, 'shipping':False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'carts':cart, 'cartItems':cartItems}
    return render(request, 'cart/cart.html', context)

def addOrder(request):
    data = json.loads(request.body)
    user = request.user
    cart = data['cart']
    firstName = data['firstName']
    lastName = data['lastName']
    email = data['email']
    phone = data['phone']
    province = data['province']
    district = data['district']
    wards = data['wards']
    address = data['address']

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
    updateCart.save()

    return JsonResponse('Order was added', safe=False)