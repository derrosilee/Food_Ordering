from django.shortcuts import render, get_object_or_404
from .models import Menu


# Create your views here.
def home(request):
    return render(request, 'index.html')


# To display page with the menu's
def menu(request):
    menulist = Menu.objects.all()
    return render(request, 'menu.html', {'menulist': menulist})


# Registration View
def register(request):
    return render(request, 'register.html')


# Login View
def login(request):
    return render(request, 'login.html')


# Product View Page
def product(request, id):
    product_desc = get_object_or_404(Menu, pk=id)
    return render(request, 'product.html', {'product_desc': product_desc})
