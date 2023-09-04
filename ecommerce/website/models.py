from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Admin(User):
    job_title = models.CharField(max_length=200)
    hire_date = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"


class Customer(User):
    phone = models.CharField(max_length=30)
    adress = models.TextField()

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Category(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name_en = models.CharField(max_length=200)
    name_ar = models.CharField(max_length=200)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.RESTRICT)


class Order(models.Model):
    create_date = models.DateTimeField(default=datetime.now())
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    status_choices = {
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered')
    }
    status = models.CharField(max_length=20, choices=status_choices)


class OrderDetails(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product_id = models.ForeignKey(Product, on_delete=models.RESTRICT)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_count = models.PositiveIntegerField()
