from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="views"),
    path('menu/', views.menu, name="Menu")
]