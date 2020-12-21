from django.shortcuts import render
from cart.models import Cart,CartItem
# Create your views here.
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer, complete=False)
        # carts = Order.objects.get(pk = customer)
        items = cart.orderitem_set.all()
        cartItems = cart.get_cart_items
    else:
        # Tao gio hang trong cho khach chua dang nhap
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'carts': cart, 'cartItems':cartItems}
    return render(request, 'checkout/checkout.html', context)