from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate , login as loginUser, logout
from app.models import GROCERY_2
from datetime import datetime
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            groceries = GROCERY_2.objects.filter(user=request.user)
            print(request.user)
            print(groceries)
            return render(request, 'index.html', context={'groceries':groceries})
        else:
            date = request.POST.get('date')
            print(date)
            if date is None:
                groceries = GROCERY_2.objects.filter(user=request.user)
                print(groceries)
                return render(request, 'index.html', context={'groceries':groceries})
            else:
                groceries = GROCERY_2.objects.filter(date=date, user=request.user)
                print(groceries)
                return render(request, 'index.html', context={'groceries':groceries})
    else:
        return redirect('login')


@login_required(login_url='login')
def add_list(request):
    if request.method == "POST":
        name = request.POST.get('name')
        print(name)
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        date = request.POST.get('date')
        grocery = GROCERY_2(name=name, quantity=quantity, status=status, date=date, user=request.user)
        print(request.user)
        grocery.save()
        return redirect("home")
    else:
        return render(request,'add.html')

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form' : form
        }
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data = request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context = {
                'form' : form
            }
            return render(request, 'login.html', context=context)

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form              
        }
        return render(request, 'signup.html', context=context)
    
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form" : form              
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=context)

def update_list(request, id):
    if request.method == "GET":
        grocery = GROCERY_2.objects.get(pk=id)
        print(grocery.date)
        return render(request,'update.html',context={'grocery':grocery})
    else:
        grocery = GROCERY_2.objects.get(pk=id)
        grocery.user = request.user
        grocery.name = request.POST.get('name')
        grocery.quantity = request.POST.get('quantity')
        grocery.status = request.POST.get('status')
        grocery.date = request.POST.get('date')
        grocery.save()
        print('update_list')
        return redirect("home")

def delete_list(request, id):
    print(id)
    GROCERY_2.objects.get(pk=id).delete()
    return redirect('home')

def signout(request):
    logout(request)
    return redirect('login')
    