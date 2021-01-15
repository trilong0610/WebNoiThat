from django.contrib import messages, auth
from django.contrib.postgres import serializers
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from product.models import Category, Product, SizeProduct
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
    hot_product = Product.objects.filter(active=True).order_by('-id')[:6]
    # best seller
    best_seller = Product.objects.filter(active=True).order_by('-amount_sell')[:6]

    all_product = Product.objects.filter(active=True)
    paginator = Paginator(all_product, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'category':category,
               'hot_product':hot_product,
               'items': items,
               'cartItems' : cartItems,
               'all_product':page_obj,
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
    hot_product = Product.objects.filter(active=True).order_by('-id')[:6]
    # best seller
    best_seller = Product.objects.filter(active=True).order_by('-amount_sell')[:6]
    paginator = Paginator(best_seller, 9)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'category':category,
               'hot_product':hot_product,
               'items': items,
               'cartItems' : cartItems,
               'all_product':page_obj,
               'best_sellers':best_seller,
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
    hot_product = Product.objects.filter(active=True).order_by('-id')[:6]
    # best seller
    best_seller = Product.objects.filter(active=True).order_by('-amount_sell')[:6]

    all_product = Product.objects.filter(active=True)

    paginator = Paginator(all_product, 9)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'category': category,
               'hot_product': hot_product,
               'items': items,
               'cartItems': cartItems,
               'all_product': page_obj,
               'best_sellers': best_seller,
               }
    return render(request, 'store/ProductGrid.html', context)

def seacrchProduct(request):
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
    hot_product = Product.objects.filter(active=True).order_by('-id')[:6]
    # best seller
    best_seller = Product.objects.filter(active=True).order_by('-amount_sell')[:6]
    if request.method == "POST":
        key = request.POST["key"]
        all_product = Product.objects.filter(title__contains=key)
    else:
        all_product = Product.objects.filter(active=True)

    context = {'category': category,
               'hot_product': hot_product,
               'items': items,
               'cartItems': cartItems,
               'all_product': all_product,
               'best_sellers': best_seller,
               }
    return render(request, 'store/ProductGrid.html', context)

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
        q = Category.objects.get( id =category_id)
        all_product = q.product_set.filter(active=True)
        category = Category.objects.all()
        # sam pham moi nhat
        hot_product = Product.objects.filter(active=True).order_by('-id')[:6]
        # best seller
        best_seller = Product.objects.filter(active=True).order_by('-amount_sell')[:6]
        paginator = Paginator(all_product, 9)  # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'category': category,
                   'items': items,
                   'cartItems': cartItems,
                   'all_product': page_obj,
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
def add_Item_To_Cart(request):
    response_data = {}
    if request.is_ajax and request.method == "POST":
        # Lay data duojc post den
        p_quantityProduct = request.POST['quantity_product']
        p_sizeProduct = request.POST['size']
        sizeProduct = SizeProduct.objects.get(id = p_sizeProduct)

        customer = request.user
        # data tra ve de
        # tao gio hang moi neu chua co
        # hoac get gio hang chua thanh toan(complete = False)
        cart, created = Cart.objects.get_or_create(user=customer, complete=False)
        cartItem, created = CartItem.objects.get_or_create(cart=cart, sizeProduct=sizeProduct)
        # Ktra so luong ton kho cua kich co do co lon hon tong sl trong gio hang + dang them hay khong
        if sizeProduct.amount >= cartItem.quantity + int(p_quantityProduct):
            cartItem.quantity = cartItem.quantity + int(p_quantityProduct)
        else:
            context = {
                'action': False,
                'nameProduct': sizeProduct.product.title,
            }
            return JsonResponse({"instance": "OutStock"}, status=400)


        cartItem.save()
        if cartItem.quantity <= 0:
            cartItem.delete()

        context = {
            'action': True,
            'nameProduct': sizeProduct.product.title,
        }
        return JsonResponse({"instance": "Success"}, status=200)

def addItemToCart(request):
    data = json.loads(request.body)
    sizeProductID = data['sizeProductID']
    quantity = data['quantity']

    customer = request.user
    sizeProduct = SizeProduct.objects.get(id=sizeProductID)
    cart, created = Cart.objects.get_or_create(user=customer, complete=False)
    cartItem, created = CartItem.objects.get_or_create(cart=cart, sizeProduct=sizeProduct)
    if sizeProduct.amount >= cartItem.quantity + int(quantity):
        cartItem.quantity = cartItem.quantity + int(quantity)
    else:
        context = {
            'outStock': True,
            'amount_product': sizeProduct.amount,
        }
        return JsonResponse(context, safe=False)
    cartItem.save()
    if cartItem.quantity <= 0:
        cartItem.delete()
    return JsonResponse('Item was added', safe=False)

def deleteProductCart(request):
    data = json.loads(request.body)
    sizeproductID = data['sizeproductID']

    customer = request.user
    sizeProduct = SizeProduct.objects.get(id=sizeproductID)
    cart, created = Cart.objects.get_or_create(user=customer, complete=False)
    cartItem, created = CartItem.objects.get_or_create(cart=cart, sizeProduct=sizeProduct)
    cartItem.quantity =  0
    cartItem.save()
    if cartItem.quantity <= 0:
        cartItem.delete()
    return JsonResponse('Item was added', safe=False)

def updateItem(request):
    data = json.loads(request.body)
    sizeProductID = data['sizeProductID']
    action = data['action']

    customer = request.user
    sizeProduct = SizeProduct.objects.get(id = sizeProductID)

    cart, created = Cart.objects.get_or_create(user = customer, complete=False)
    cartItem, created = CartItem.objects.get_or_create(cart=cart, sizeProduct=sizeProduct)
    if action == 'add':
        if sizeProduct.amount > cartItem.quantity:
            cartItem.quantity = (cartItem.quantity + 1)
        else:
            context = {
                'outStock': True,
                'amount_product': sizeProduct.amount,
            }
            return JsonResponse(context, safe=False)

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
    hot_product = Product.objects.filter(active=True).order_by('id')[:6]
    # best seller
    best_seller = Product.objects.filter(active=True).order_by('-amount_sell')[:6]
    # sam pham moi nhat
    all_product = Product.objects.filter(active=True).order_by('-id')
    paginator = Paginator(all_product, 9)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'category':category,
               'hot_product':hot_product,
               'items': items,
               'best_sellers':best_seller,
               'cartItems' : cartItems,
               'all_product':page_obj,
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
    hot_product = Product.objects.filter(active=True).order_by('-id')[:6]
    # best seller
    best_seller = Product.objects.filter(active=True).order_by('-amount_sell')


    all_product = Product.objects.filter(active=True)
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

def get_absolute_url_product(self):
    from django.urls import reverse
    return reverse('store:detailProduct', args=[str(self.id)])