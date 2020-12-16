from django.contrib.auth.models import User
from django.shortcuts import render

from order.models import Order,OrderItem
# Create your views here.
def cart(request):
    if request.user.is_authenticated:
        customer = User.objects.get(pk = request.user.id)
        order, created = Order.objects.get_or_create( user = request.user, complete=False)
        # order = Order.objects.get(pk = customer)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0, 'shipping':False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order':order, 'cartItems':cartItems}
    return render(request, 'cart/cart.html', context)
