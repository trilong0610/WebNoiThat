from django.contrib.auth.models import User
from django.shortcuts import render

from cart.models import Cart,CartItem
# Create your views here.
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
