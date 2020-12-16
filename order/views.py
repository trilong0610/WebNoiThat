from django.contrib.auth.models import User
from django.shortcuts import render

from order.models import Order


def shipping_status(request):
    customer = User.objects.get(pk=request.user.id)
    order, created = Order.objects.get_or_create(user=request.user, complete=False)
    status = Order.shipping
    context = {'order_shipping':order, 'status':status}
    return render(request,'order/shipping_status.html', context)