from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomerForm

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
            login_url = reverse("login")
            return redirect(login_url)
        else:
            return render(request, "website/register.html", {"form": form})


class Login(View):
    def get(self, request):
        return render(request, "website/login.html")


class Logout(View):
    def get(self, request):
        pass
