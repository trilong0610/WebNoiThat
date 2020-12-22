from django.contrib.auth.models import User
from django.shortcuts import render

from cart.models import Cart

def view_cart(request):
    user = request.user
    cart = Cart.objects.get(user = user, complete=False)
    context = {
        "cart":cart
    }
    return render(request, 'cart/Cart.html', context)
def shipping_status(request):
    current_user = request.user
    cart = Cart.objects.filter(user_id = current_user.id)
    status = Cart.shipping
    context = {'order_shipping':cart, 'status_ship':status}
    return render(request, 'order/order_shipping.html', context)