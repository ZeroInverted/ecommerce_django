from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, "website/index.html")


class Register(View):
    def get(self, request):
        return render(request, "website/register.html")


class Login(View):
    def get(self, request):
        return render(request, "website/login.html")


class Logout(View):
    def get(self, request):
        pass
