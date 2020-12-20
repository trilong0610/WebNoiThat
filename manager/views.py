import json

from django.contrib import auth
from django.contrib.auth import decorators
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from order.models import Order
from product.models import Product
from product.forms import ProductForm,CategoryForm
from supplier.models import Supplier
from supplier.forms import  SupplierForm
from purchase.forms import PurchaseProductForm
from django.contrib.auth.models import User, Permission
from datetime import datetime
# Create your views here.
from django.http import HttpResponse, JsonResponse


@decorators.login_required(login_url='/login/')
def home(request):
    perm = ["A"]
    if request.user.has_perm('Product.add_product'):
        perm.append("add_product")
    context = {"perm": perm}
    return render(request, "manager/base.html", context)

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
            return render(request, "manager/manage_Action.html", {"add_product": product})
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
            # Gui OBJ User hien tai de check permission
            request_user = User.objects.get(id = request.user.id)
            context = {'users': list_users, 'request_user': request_user}
            return render(request, 'manager/view_user.html', context)

# Xem quyen user
class gains_permission(LoginRequiredMixin,View):
    login_url = '/login/'
    permission_required('auth.change_user')
    def get(self, request, user_id):
        # Neu la superuser moi cho vao trang phan quyen
        if request.user.is_superuser:
            user = User.objects.get(id=user_id)
            return render(request, 'manager/gains_permission.html', {'user_permission':user})
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

class update_shipping(View):
    def get(self,request):
        customer = User.objects.get(pk=request.user.id)
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        status = Order.shipping
        context = {'order_shipping':order, 'status':status}
        return render(request,'manager/shipping.html', context)
    def post(self, request):
        customer = User.objects.get(id = request.user.id)
        # order, created = Order.objects.get_or_create(user=request.user, complete=False)
        data = request.POST["shipping"]
        Order.objects.filter(id = data).update(complete = True)
        order = Order.objects.get(id = data)
        status = Order.shipping
        context = {'order_shipping': order, 'status': status}
        return render(request,'manager/shipping.html', context)


#load tat ca san pham len bang tren dashboard.html
def dashboard(request):
    products = Product.objects.all()
    return render(request, 'manager/dashboard.html', {'products':products})
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