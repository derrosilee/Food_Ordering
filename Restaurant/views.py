from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


# To display page with the menu's
def menu(request):
    return render(request, 'menu.html')

# Registartion View
def register(request):
    return render(request, 'register.html')