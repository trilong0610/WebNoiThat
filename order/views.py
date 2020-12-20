from django.contrib.auth.models import User
from django.shortcuts import render

from order.models import Order


def shipping_status(request):
    current_user = request.user
    order = Order.objects.filter(user_id = current_user.id)
    status = Order.shipping
    context = {'order_shipping':order, 'status_ship':status}
    return render(request,'order/shipping_status.html', context)