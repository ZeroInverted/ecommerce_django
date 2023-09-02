from django.contrib import admin
from .models import Admin, Customer
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Admin, UserAdmin)
admin.site.register(Customer)
