from django.shortcuts import render
from order.models import Order,OrderItem
# Create your views here.
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # order = Order.objects.get(pk = customer)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        # Tao gio hang trong cho khach chua dang nhap
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems':cartItems}
    return render(request, 'checkout/checkout.html', context)