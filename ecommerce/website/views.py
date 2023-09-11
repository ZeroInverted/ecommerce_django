from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomerForm
from .models import Product, Customer, Order
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.db.models import Q

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
        # Check if user is logged in or not
        if request.user.is_authenticated:
            # If user is logged in, fetch user from the Customer db
            customer = Customer.objects.get(user_ptr=request.user)
            # Fetch user's order if it exists, if not, create it
            order, created_order = Order.objects.get_or_create(
                customer_id=customer, status="Pending")
            # Reverse lookup through the FK defined in orderdetails to get all orderdetails
            items = order.orderdetails_set.all()
        else:
            items = []
            order = {"calculate_cart_total": 0, "calculate_items_quantity": 0}
        return render(request, "website/cart.html", {"items": items, "order": order})


class Orders(View):
    def get(self, request):
        if request.user.is_authenticated:
            # If user is logged in, fetch user from the Customer db
            customer = Customer.objects.get(user_ptr=request.user)
            # Fetch user's order if it exists, if not, create it
            orders = Order.objects.filter(customer_id=customer)
            print(orders)
        else:
            orders = {"id": 0, "status": 0}
        return render(request, "website/orders.html", {"orders": orders})

    @csrf_exempt
    def post(self, request):
        customer = Customer.objects.get(user_ptr=request.user)
        body_data = json.loads(request.body)
        if body_data:
            filter_field = body_data['filter_field']
            customer_id_cond = Q(customer_id=customer)
            status_cond = Q(status=filter_field)
            combined_cond = customer_id_cond & status_cond
            if filter_field != "all":
                orders = Order.objects.filter(combined_cond)
            else:
                orders = Order.objects.filter(customer_id_cond)
            serial_orders = serializers.serialize("json", orders)
            print(serial_orders)

            return JsonResponse(serial_orders, safe=False)


class Checkout(View):
    def get(self, request):
        return render(request, "website/store.html")
