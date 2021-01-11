from django.shortcuts import render
from cart.models import Cart,CartItem
# Create your views here.
from user.models import Address, Province


def checkout(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user = user, complete=False)
    address, created = Address.objects.get_or_create(user = user)
    province = Province.objects.all()
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, complete=False)
        items = cart.cartitem_set.all()
        cartItems = cart.get_cart_items
    else:
        items = []
        cart = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = cart['get_cart_items']
    context = {
        "cart":cart,
        'user':user,
        'address':address,
        'province':province,
        'items':items,
        'cartItems':cartItems,
    }
    return render(request, 'checkout/Checkout.html', context)