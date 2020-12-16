from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.contrib import messages

# Dic check login def
from django.contrib.auth import authenticate, login, decorators
# Dic check login class base view
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import  CreateUserForm
from django.http import HttpResponseRedirect


def RegisterPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            messages.success(request,'Account was created for ' + user)
            return redirect('login')
    context = {'form': form}
    return  render(request, 'User/register.html', context)


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'User/login.html', context)

def LogoutUser(request):
    logout(request)
    return redirect('login')




