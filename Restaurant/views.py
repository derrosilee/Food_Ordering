from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


# To display page with the menu's
def menu(request):
    return render(request, 'menu.html')


# Registration View
def register(request):
    return render(request, 'register.html')


# Login View
def login(request):
    return render(request, 'login.html')


# Product View Page
def product(request):
    return render(request, 'product.html')