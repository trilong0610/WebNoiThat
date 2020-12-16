from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from product.models import Category,Product
from product.forms import ProductForm,CategoryForm
from django.http import HttpResponse
from order.models import Order,ShippingAddress,OrderItem
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, decorators, logout
from django.contrib.auth.decorators import login_required
# Dic check login class base view
from django.contrib.auth.mixins import LoginRequiredMixin
import json
# Create your views here.
# Xem hang hoa
@login_required(login_url='login')
def store(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    category = Category.objects.all()
    product_main = Product.objects.all()
    context = {'category':category, 'items': items, 'cartItems' : cartItems, 'products':product_main}

    return render(request, 'store/main.html', context)

# def category(request):
#     category = Category.objects.all()
#     return render(request, 'store/main.html', {'category':category})
# def store(request):
#     context = {}
#     return render(request, 'store/store.html', context)
class view_category(View):
    def get(self, request, category_id):
        if request.user.is_authenticated:
            customer = request.user.id
            order, created = Order.objects.get_or_create(user_id=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cartItems = order['get_cart_items']
        q = Category.objects.get(pk=category_id)
        category = Category.objects.all()

        context = {'category': category, "product": q, 'items': items, 'cartItems': cartItems}
        return render(request, 'store/store.html', context)

# def view_category(request, category_id):
#     # list_product = Category.objects.get(pk=category_id)
#     q = Category.objects.get(pk=category_id)
#     return render(request, 'store/list_product.html', {"list_product": q})

# def cart(request):
#     context = {}
#     return render(request, 'store/../cart/templates/cart/cart.html', context)



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
def updateItem(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    print('Action:', action)
    print('productId:', productID)

    customer = request.user
    product = Product.objects.get(id = productID)
    order, created = Order.objects.get_or_create(user = customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)