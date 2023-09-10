from django.contrib import admin
from .models import Admin, Customer, Product, Order, OrderDetails, Category
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Category)
