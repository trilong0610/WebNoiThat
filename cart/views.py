from django.contrib.auth.models import User
from django.shortcuts import render
from cart.models import Cart
from product.models import Category


def view_cart(request):
    user = request.user
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, complete=False)
        items = cart.cartitem_set.all()
        cartItems = cart.get_cart_items
    else:
        items = []
        cart = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = cart['get_cart_items']
    cart = Cart.objects.get(user = user, complete=False)
    category = Category.objects.all()
    context = {
        "cart":cart,
        'cartItems':cartItems,
        'category': category,
    }
    return render(request, 'cart/Cart.html', context)
def shipping_status(request):
    current_user = request.user
    cart = Cart.objects.filter(user_id = current_user.id)
    status = Cart.shipping
    context = {'order_shipping':cart, 'status_ship':status}
    return render(request, 'order/order_shipping.html', context)