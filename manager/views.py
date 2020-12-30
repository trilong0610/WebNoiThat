import json

from django.contrib import auth
from django.contrib.auth import decorators
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from cart.models import Cart
from product.models import Product
from product.forms import ProductForm,CategoryForm
from supplier.models import Supplier
from supplier.forms import  SupplierForm
from purchase.forms import PurchaseProductForm
from django.contrib.auth.models import User, Permission
from datetime import datetime
# Create your views here.
from django.http import HttpResponse, JsonResponse


class home(PermissionRequiredMixin,View):
    permission_required = ('auth.view_user')
    def get(self,request):
        # Neu la superuser moi cho vao trang phan quyen
            list_users = User.objects.all()
            # Gui OBJ user hien tai de check permission
            request_user = User.objects.get(id = request.user.id)
            context = {'users': list_users, 'request_user': request_user}
            return render(request, 'manager/ListUser.html', context)

# Nhap San Pham Tu NCC
class purchase_product(LoginRequiredMixin,View):
    def get(self, request):
        form = PurchaseProductForm()
        return render(request, "manager/purchase_product.html", {'form':form})
    def post(self,request):
        form = PurchaseProductForm(request.POST)
        form.complete = False
        if form.is_valid():
            form.save()
            return redirect('/manager/')
        else:
            return HttpResponse('Sai Cu Phap')

# Quan Li San Pham
class add_category(LoginRequiredMixin,View):
    def get(self,request):
        category = CategoryForm()
        return render(request, "manager/manage_Action.html", {"add_category": category})
    def post(self,request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/manager/')
        else:
            return HttpResponse("Sai cu phap")

class add_product(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request):
            product = ProductForm()
            return render(request, "manager/AddProduct.html", {"add_product": product})
    def post(self,request):
        form = ProductForm(data = request.POST, files= request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/manager/')
        else:
            return HttpResponse("Sai cu phap")

# Xem danh sach user
class view_User(PermissionRequiredMixin,View):
    permission_required = ('auth.view_user')
    def get(self,request):
        # Neu la superuser moi cho vao trang phan quyen
            list_users = User.objects.all()
            # Gui OBJ user hien tai de check permission
            request_user = User.objects.get(id = request.user.id)
            context = {'users': list_users, 'request_user': request_user}
            return render(request, 'manager/ListUser.html', context)

# Xem quyen user
class gains_permission(LoginRequiredMixin,View):
    login_url = '/login/'
    permission_required('auth.change_user')
    def get(self, request, user_id):
        # Neu la superuser moi cho vao trang phan quyen
        if request.user.is_superuser:
            user = User.objects.get(id=user_id)
            return render(request, 'manager/Permission.html', {'user_permission':user})
        else:
            return HttpResponse("Ban khong co quyen truy cap")

# Thay doi quyen user(chi user co quyen thay doi thong tin user moi duoc vao)
@permission_required('auth.change_user')
def updatePermission(request):
        data = json.loads(request.body)
        user = data['user']
        permission = data['permission']
        action = data['action']
        print('user:', user)
        print('permission:', permission)
        print('action:', action)
        user_change_perm = User.objects.get(username = user)
        if action == 'add':
            permission_add = Permission.objects.get(name=permission)
            user_change_perm.user_permissions.add(permission_add)
            return JsonResponse('Permission was add', safe=False)
        elif action == 'remove':
            permission_add = Permission.objects.get(name=permission)
            user_change_perm.user_permissions.remove(permission_add)
            return JsonResponse('Permission was remove', safe=False)
        return JsonResponse('Permission changged failed', safe=False)


class view_shipping(View):
    def get(self,request):
        current_user = request.user
        cart = Cart.objects.filter(user_id=current_user.id)
        status = Cart.shipping
        context = {'order_shipping':cart, 'status':status}
        return render(request, 'manager/shipping_control.html', context)

def updateShipping(request):
    data = json.loads(request.body)
    orderid = data['orderid']
    status = data['status']
    cart = Cart.objects.get(id = orderid)
    cart.status = status
    cart.save()
    status = Cart.shipping
    return JsonResponse('Update shipping complete', safe=False)

#load tat ca san pham len bang tren dashboard.html
def test(request):
    context = {
    }
    return  render(request,'manager/test.html', context)

def dashboard(request):
    products = Product.objects.all()
    return render(request, 'manager/ProductControl.html', {'products':products})

# xoa, sua san pham
def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'manager/edit_product.html', {'product':product})

def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance = product)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'manager/edit_product.html', {'product':product})

def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/")