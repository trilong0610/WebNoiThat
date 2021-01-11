import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from cart.models import Cart, CartItem
from product.models import Category, Product, SizeProduct


def view_cart(request):
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

# sua so luong theo input
def editItemQuantity(request):
    data = json.loads(request.body)
    sizeProductID = data['sizeProductID']
    quantity = data['quantity']

    customer = request.user
    sizeProduct = SizeProduct.objects.get(id=sizeProductID)
    if sizeProduct.amount < 0 or sizeProduct.amount < int(quantity):
        context = {
            'outStock': True,
            'amount_product': sizeProduct.amount,
        }
        return JsonResponse(context, safe=False)
    cart, created = Cart.objects.get_or_create(user=customer, complete=False)
    cartItem, created = CartItem.objects.get_or_create(cart=cart, sizeProduct=sizeProduct)

    cartItem.quantity = int(quantity)
    cartItem.save()

    if cartItem.quantity <= 0:
        cartItem.delete()
    return JsonResponse('Item was added', safe=False)