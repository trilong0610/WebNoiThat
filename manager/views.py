import json
from itertools import product
from math import prod

from django.contrib import auth
from django.contrib.auth import decorators
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from cart.models import Cart
from order.models import Order
from product.models import Product, Category
from product.forms import ProductForm,CategoryForm
from purchase.models import PurchaseProduct
from supplier.models import Supplier
from supplier.forms import  SupplierForm
from purchase.forms import PurchaseProductForm
from django.contrib.auth.models import User, Permission
from datetime import datetime
# Create your views here.
from django.http import HttpResponse, JsonResponse


class home(View):
    def get(self,request):
        # Neu la superuser moi cho vao trang phan quyen
            list_users = User.objects.all()
            # Gui OBJ user hien tai de check permission
            request_user = User.objects.get(id = request.user.id)
            context = {'users': list_users, 'request_user': request_user}
            return render(request, 'manager/userControl/UserControl.html', context)

# Nhap San Pham Tu NCC
class purchaseProduct(LoginRequiredMixin,View):
    def get(self, request):
        form = PurchaseProductForm()
        user = request.user
        context = {
            'form':form,
            'user':user,
        }
        return render(request, "manager/purchaseControl/PurchaseProduct.html", context)
    def post(self,request):
        form = PurchaseProductForm(data = request.POST)
        user = request.user
        amount = request.POST["amount"]
        form.user = user
        form.amount = amount
        if form.is_valid():
            form.save()
            return redirect('manager:viewPurchase')
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

            return render(request, "manager/productControl/AddProduct.html", {"product": product})
    def post(self,request):
        form = ProductForm(data = request.POST, files= request.FILES)
        form.price = request.POST["price"]
        if form.is_valid():
            form.save()
            return redirect('manager:product_control')
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
            return render(request, 'manager/userControl/UserControl.html', context)

# Xem quyen user
class gains_permission(LoginRequiredMixin,View):
    login_url = '/login/'
    permission_required('auth.change_user')
    def get(self, request, user_id):
        # Neu la superuser moi cho vao trang phan quyen
        if request.user.is_superuser:
            user = User.objects.get(id=user_id)
            context =  {
                'user':user,
                'permission': user.get_all_permissions()
            }
            return render(request, 'manager/userControl/Permission.html', context)
        else:
            return HttpResponse("Ban khong co quyen truy cap")

# Thay doi quyen user(chi user co quyen thay doi thong tin user moi duoc vao)
def updatePermission(request):
        data = json.loads(request.body)
        user = data['user']
        permission = data['permission']
        action = data['action']

        user_change_perm = User.objects.get(id = user)

        if action == 'add':
            permission_add = Permission.objects.get(name=permission)
            user_change_perm.user_permissions.add(permission_add)
            context = {
                'action':action,
                'permission':permission,

            }
            return JsonResponse(context, safe=False)
        elif action == 'remove':
            permission_add = Permission.objects.get(name=permission)
            user_change_perm.user_permissions.remove(permission_add)
            context = {
                'action': action,
                'permission': permission,

            }
            return JsonResponse(context, safe=False)
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
    return render(request, 'manager/productControl/ProductControl.html', {'products':products})

# xoa, sua san pham
class editProduct(View):
    def get(self, request, product_id):
        detail = Product.objects.get(id= product_id)
        category = Category.objects.all()
        context = {
            'product': detail,
            'category': category,
        }
        return render(request, 'manager/productControl/EditProduct.html', context)
    def post(self,request, product_id):
        productUpdate = Product.objects.get(id = product_id)
        categoryUpdate = Category.objects.get(id = request.POST["category_id"])
        category = Category.objects.all()

        productUpdate.category = categoryUpdate
        productUpdate.title = request.POST["title"]
        productUpdate.price = request.POST["price"]
        productUpdate.description = request.POST["description"]
        productUpdate.active = request.POST["active"]

        productUpdate.save()
        context = {
            'product': productUpdate,
            'category': category,
        }
        return redirect('manager:product_control')


def register(request):
    if request.method == 'POST':
        username = request.POST["user"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2 and password1 != '' and password2 != '':
            user = User.objects.create_user(username=username, email=email, password=password2)
            return render(request, 'user/RegisterSuccess.html', {'username': user.username})
        else:
            return render(request, 'manager/userControl/RegisterAccount.html', {'error': 0})
    context = {}
    return render(request, 'manager/userControl/RegisterAccount.html', context)

class editUser(View):
    def get(self, request, user_id):
        userEdit = User.objects.get( id = user_id )
        context = {
            'userEdit':userEdit,
        }
        return render(request, 'manager/userControl/EditUser.html', context)
    def post(self, request, user_id):
        userEdit = User.objects.get( id = user_id )
        pusername = request.POST['username']
        pfirstName = request.POST['first_name']
        plastName = request.POST['last_name']
        pemail = request.POST['email']
        if pusername != userEdit.username:
            userEdit.username = pusername
        userEdit.first_name = pfirstName
        userEdit.last_name = plastName
        userEdit.email = pemail
        userEdit.save()
        userEditted = User.objects.get(id=user_id)
        context = {
            'userEdit': userEditted,
        }
        return render(request, 'manager/userControl/EditUser.html', context)

def destroyUser(request, user_id):
    userEdit = User.objects.get( id = user_id )
    userEdit.delete()
    return redirect('manager:view_user')
# ------Purchase-----------
def viewPurchaseProduct(request):
    purchase = PurchaseProduct.objects.all()
    context = {
        'purchase':purchase
    }
    return render(request, 'manager/purchaseControl/PurchaseProductControl.html', context)

def destroyPurchase(request, purchase_id):
    purchase = PurchaseProduct.objects.get( id = purchase_id )
    purchase.delete()
    return redirect('manager:viewPurchase')

class editPurchase(View):
    def get(self, request, purchase_id):
        supplier = Supplier.objects.all()
        purchase = PurchaseProduct.objects.get(id = purchase_id)
        product = Product.objects.get(id = purchase.product.id)
        context = {
            'product': product,
            'supplier': supplier,
            'purchase':purchase,
        }
        return render(request, 'manager/purchaseControl/EditPurchase.html', context)
    def post(self,request, purchase_id):
        purchaseUpdate = PurchaseProduct.objects.get(id = purchase_id)
        supplier = Supplier.objects.get(id = request.POST["supplier_id"])
        product = Product.objects.get(id = request.POST["product_id"])

        purchaseUpdate.supplier = supplier
        purchaseUpdate.product = product
        purchaseUpdate.amount = request.POST["amount"]

        if purchaseUpdate.complete != True:
            purchaseUpdate.complete = request.POST["complete"]
            product.amount = product.amount + int(purchaseUpdate.amount)
            product.save()
        purchaseUpdate.save()
        return redirect('manager:viewPurchase')

class orderControl(View):
    def get(self, request):
        order = Order.objects.all().order_by('-id')
        revune = 0
        for items in order:
            revune = revune + items.cart.get_cart_total
        context = {
            'order':order,
            'revune':revune
        }
        return render(request, 'manager/orderControl/OrderControl.html', context)
    def post(self, request):
        searchOrder = request.POST.get('searchOrder')
        revune = 0
        if searchOrder:
            # Tim theo id
            order = Order.objects.get(id = int(searchOrder))
            revune = revune + int(order.cart.get_cart_total)
        else:
            fromDate = request.POST["fromDate"]
            toDate = request.POST["toDate"]
            order = Order.objects.filter(date_ordered__range=[fromDate, toDate]).order_by('-id')
            for items in order:
                    revune = revune + int(items.cart.get_cart_total)


        context = {
            'order': order,
            'revune': revune
        }
        return render(request, 'manager/orderControl/OrderControl.html', context)


class editOrder(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        context = {
            'order':order
        }
        return render(request, 'manager/orderControl/EditOrder.html', context)
    def post(self,request, order_id):
        user = User.objects.get(username= request.POST['user'])
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phone']
        province = request.POST['province']
        district = request.POST['district']
        wards = request.POST['wards']
        address = request.POST['address']
        status = request.POST['status']


        order = Order.objects.get(id=order_id )

        order.first_name = firstName
        order.last_name = lastName
        order.email = email
        order.phone = phone
        order.province = province
        order.district = district
        order.wards = wards
        order.address = address
        order.date_ordered = datetime.now()
        order.transaction_id = order.cart.id
        order.status = status
        order.save()

        # cap nhat so luong da ban va ton kho cua san pham
        cart = Cart.objects.get(id = order.cart.id)
        for item in cart.cartitem_set.all():
            product = Product.objects.get(id = item.product.id)
            product.amount = product.amount - item.quantity
            product.amount_sell = product.amount_sell + item.quantity
            product.save()
        context = {'cart_id':order.cart.id}
        return redirect('manager:orderControl')

# -----------Category--------------------

def categoryControl(request):
    category = Category.objects.all()
    context = {
        'category':category
    }
    return render(request, 'manager/categoryControl/CategoryControl.html', context)

class addCategory(View):
    def get(self, request):
        form = CategoryForm()
        context = {
            "form":form
        }
        return render(request, 'manager/categoryControl/AddCategory.html', context)
    def post(self, request):
        form = CategoryForm(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager:categoryControl')
        else:
            return HttpResponse('Sai Cu Phap')


class editCategory(View):
    def get(self, request, category_id):
        category = Category.objects.get(id = category_id)

        context = {
            "scategory":category
        }
        return render(request, 'manager/categoryControl/EditCategory.html', context)
    def post(self, request, category_id):

        category = Category.objects.get(id = category_id)

        title = request.POST["title"]
        description = request.POST["description"]
        active = request.POST["active"]

        category.title = title
        category.description = description
        category.active = active
        category.save()
        return redirect("manager:categoryControl")

# Doanh thu
class revenue(View):
    def get(self, request):
        order = Order.objects.all().order_by('-id')
        revune = 0
        for items in order:
            revune = revune + items.cart.get_cart_total
        context = {
            'order':order,
            'revune':revune
        }
        return render(request, 'manager/Revenue.html', context)
    def post(self, request):
        fromDate = request.POST["fromDate"]
        toDate = request.POST["toDate"]
        revune = 0
        if fromDate == toDate:
            order = Order.objects.filter(date_ordered=toDate).order_by('-id')
            for items in order:
                revune = revune + int(items.cart.get_cart_total)
        else:
            order = Order.objects.filter(date_ordered__range=[fromDate, toDate]).order_by('-id')
            for items in order:
                revune = revune + int(items.cart.get_cart_total)
        context = {
            'order': order,
            'revune': revune
        }
        return render(request, 'manager/Revenue.html', context)
