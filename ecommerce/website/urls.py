from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("register", views.Register.as_view(), name="register"),
    path("login", views.Login.as_view(), name="login"),
    path("logout", views.Logout.as_view(), name="logout"),
    path("store", views.Store.as_view(), name="store"),
    path("cart", views.Cart.as_view(), name="cart"),
    path("checkout", views.Checkout.as_view(), name="checkout"),
    path("orders", views.Orders.as_view(), name="orders")
]
