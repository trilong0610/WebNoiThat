from django.contrib.auth.models import User
from django.shortcuts import render

from cart.models import Cart


def shipping_status(request):
    current_user = request.user
    cart = Cart.objects.filter(user_id = current_user.id)
    status = Cart.shipping
    context = {'order_shipping':cart, 'status_ship':status}
    return render(request, 'order/order_shipping.html', context)