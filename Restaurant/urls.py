from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('product/', views.product, name="product")  # Replace with I'd View
]
