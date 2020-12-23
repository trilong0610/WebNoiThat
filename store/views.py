from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from product.models import Category,Product
from product.forms import ProductForm,CategoryForm
from django.http import HttpResponse
from cart.models import Cart, ShippingAddress, CartItem
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, decorators, logout
from django.contrib.auth.decorators import login_required
# Dic check login class base view
from django.contrib.auth.mixins import LoginRequiredMixin
import json
# Create your views here.
# Xem hang hoa

def view_product(request):
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, complete=False)
        items = cart.cartitem_set.all()
        cartItems = cart.get_cart_items
    else:
        items = []
        cart = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = cart['get_cart_items']
    category = Category.objects.all()
    # sam pham moi nhat
    hot_product = Product.objects.all().order_by('-id')[:6]
    # best seller
    best_seller = Product.objects.all().order_by('-amount_sell')[:6]

    all_product = Product.objects.all()

    context = {'category':category,
               'hot_product':hot_product,
               'items': items,
               'cartItems' : cartItems,
               'all_product':all_product,
               'best_sellers':best_seller,
               }
    return render(request, 'store/ProductGrid.html', context)

# Nhieu nguoi mua
def most_popular(request):
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, complete=False)
        items = cart.cartitem_set.all()
        cartItems = cart.get_cart_items
    else:
        items = []
        cart = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = cart['get_cart_items']
    category = Category.objects.all()
    # sam pham moi nhat
    hot_product = Product.objects.all().order_by('-id')[:6]
    # best seller
    best_seller = Product.objects.all().order_by('amount_sell')[:6]

    context = {'category':category,
               'hot_product':hot_product,
               'items': items,
               'cartItems' : cartItems,
               'all_product':best_seller,
               }
    return render(request, 'store/ProductGrid.html', context)

def home(request):
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, complete=False)
        items = cart.cartitem_set.all()
        cartItems = cart.get_cart_items
    else:
        items = []
        cart = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = cart['get_cart_items']
    category = Category.objects.all()
    # sam pham moi nhat
    hot_product = Product.objects.all().order_by('-id')[:3]
    product_main = Product.objects.all()
    context = {'category':category,'hot_product':hot_product, 'items': items, 'cartItems' : cartItems, 'products':product_main}
    return render(request, 'store/Home.html', context)


class view_category(View):
    def get(self, request, category_id):
        if request.user.is_authenticated:
            customer = request.user.id
            cart, created = Cart.objects.get_or_create(user_id=customer, complete=False)
            items = cart.cartitem_set.all()
            cartItems = cart.get_cart_items
        else:
            items = []
            cart = {'get_cart_total': 0, 'get_cart_items': 0}
            cartItems = cart['get_cart_items']
        q = Category.objects.get(pk=category_id)
        all_product = q.product_set.all()
        category = Category.objects.all()
        # sam pham moi nhat
        hot_product = Product.objects.all().order_by('-id')[:6]
        # best seller
        best_seller = Product.objects.all().order_by('-amount_sell')[:6]
        context = {'category': category,
                   'items': items,
                   'cartItems': cartItems,
                   'all_product': all_product,
                   'best_sellers': best_seller,
                   'hot_product':hot_product,
                   'items': items
                   }
        return render(request, 'store/ProductGrid.html', context)


# quan li hang hoa
class manage(View):
    # login_url = '/login/'
    def get(self, request):
        # product = ProductForm()
        # action_id = {"action_product" : 1,"action_category" : 2}
        return render(request, "store/manage.html", {"action_product" : '1',"action_category" : '2'})


class manageAction(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request, action_id):
        if action_id == 1:
            product = ProductForm()
            return render(request, "store/manage_Action.html", {"add_product": product})
        if  action_id == 2:
            category = CategoryForm()
            return render(request, "store/manage_Action.html", {"add_category": category})
    def post(self,request, action_id):
        if action_id == 1:
            form = ProductForm(data = request.POST, files= request.FILES)
        if action_id == 2:
            form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/manage/')
        else:
            return HttpResponse("Sai cu phap")

# Dang xuat
def logout(request):
    auth.logout(request)
    messages.success(request, 'Profile details updated.')
    return redirect("/")

# Them item vao gio hang
def addItemToCart(request):
    data = json.loads(request.body)
    productID = data['productID']
    quantity = data['quantity']
    print('quantity:', quantity)
    print('productId:', productID)
    customer = request.user
    product = Product.objects.get(id = productID)
    cart, created = Cart.objects.get_or_create(user = customer, complete=False)
    cartItem, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cartItem.quantity = int(quantity)
    cartItem.save()
    if cartItem.quantity <= 0:
        cartItem.delete()
    return JsonResponse('Item was added', safe=False)


def updateItem(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    print('Action:', action)
    print('productId:', productID)
    customer = request.user
    product = Product.objects.get(id = productID)
    cart, created = Cart.objects.get_or_create(user = customer, complete=False)
    cartItem, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if action == 'add':
        cartItem.quantity = (cartItem.quantity + 1)
    elif action == 'remove':
        cartItem.quantity = (cartItem.quantity - 1)
    cartItem.save()
    if cartItem.quantity <= 0:
        cartItem.delete()
    return JsonResponse('Item was added', safe=False)
#them, xoa, sua san pham

# Xem san pham

# San pham moi
def hot_product(request):
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, complete=False)
        items = cart.cartitem_set.all()
        cartItems = cart.get_cart_items
    else:
        items = []
        cart = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = cart['get_cart_items']
    category = Category.objects.all()
    # sam pham moi nhat
    all_product = Product.objects.all().order_by('-id')[:10]
    context = {'category':category,
               'hot_product':hot_product,
               'items': items,
               'cartItems' : cartItems,
               'all_product':all_product,
               }
    return render(request, 'store/ProductGrid.html', context)

# lien hệ
def contact(request):
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
        'cartItems':cartItems
    }
    return render(request, 'store/Contact.html')

def detailProduct(request, product_id):
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, complete=False)
        items = cart.cartitem_set.all()
        cartItems = cart.get_cart_items
    else:
        items = []
        cart = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = cart['get_cart_items']
    category = Category.objects.all()
    # sam pham moi nhat
    hot_product = Product.objects.all().order_by('-id')[:6]
    # best seller
    best_seller = Product.objects.all().order_by('-amount_sell')[:6]

    all_product = Product.objects.all()
    detail = Product.objects.get(id=product_id)
    context = {'category':category,
               'hot_product':hot_product,
               'items': items,
               'cartItems' : cartItems,
               'all_product':all_product,
               'best_sellers':best_seller,
               'product': detail
               }
    return render(request, 'store/SingleProduct.html', context)
