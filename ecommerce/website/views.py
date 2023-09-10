from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomerForm
from .models import Product

# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, "website/index.html")


class Register(View):

    def get(self, request):
        form = CustomerForm()
        return render(request, "website/register.html", {"form": form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("email")
            messages.success(
                request, 'Account was registered successfully! Username is ' + str(user))
            login_url = reverse("login")
            return redirect(login_url)
        else:
            return render(request, "website/register.html", {"form": form})


class Login(View):
    def get(self, request):
        return render(request, "website/login.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, "Logged in successfully as " + str(username))
            home_url = reverse("home")
            return redirect(home_url)
        # if user doesn't exist in db
        else:
            messages.error(request, "Failed to login, please try again")
            return render(request, "website/login.html")


class Logout(View):
    def get(self, request):
        pass


class Store(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "website/store.html", {"products": products})


class Cart(View):
    def get(self, request):
        return render(request, "website/cart.html")


class Checkout(View):
    def get(self, request):
        return render(request, "website/store.html")
