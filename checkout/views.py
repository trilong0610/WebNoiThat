from django.shortcuts import render
from cart.models import Cart,CartItem
# Create your views here.
from user.models import Address


def checkout(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user = user, complete=False)
    address, created = Address.objects.get_or_create(user = user)
    context = {"cart":cart,
               'user':user,
               'address':address,
               }
    return render(request, 'checkout/Checkout.html', context)