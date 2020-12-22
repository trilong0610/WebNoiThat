from django.shortcuts import render
from cart.models import Cart,CartItem
# Create your views here.
def checkout(request):
    user = request.user
    cart = Cart.objects.get(user = user, complete=False)
    context = {"cart":cart}
    return render(request, 'checkout/Checkout.html', context)