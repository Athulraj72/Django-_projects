from django.shortcuts import render,redirect
from .models import Category
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')
def category(request):
    item=Category.objects.all()
    return render(request,'category.html',{'item':item})
def product(request,i):
    c = Category.objects.get(id=i)
    p = Product.objects.filter(category=c)

    # p=Product.objects.filter(category__id=i)


    return render(request,'product.html',{'p':p,'c':c})

def details(request,i):
    p = Product.objects.get(id=i)
    return render(request,'details.html',{'p':p})

def register(request):
    if (request.method == 'POST'):
        u = request.POST['u']
        p = request.POST['p']
        cp=request.POST['c']
        fn = request.POST['f']
        ln = request.POST['l']
        e = request.POST['e']

        if cp==p:
            u = User.objects.create_user(username=u, password=p, first_name=fn, last_name=ln, email=e)
            u.save()
            return redirect('shop:home')
        else:
            messages.error(request, 'Passwords are not same')

    return render(request,'register.html')

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']

        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('shop:category')
        else:
            messages.error(request, "Invalid Entry")

    return render(request,'login.html')
@login_required()
def user_logout(request):
    logout(request)
    return redirect('shop:home')