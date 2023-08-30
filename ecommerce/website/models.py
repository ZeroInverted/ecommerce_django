from django.db import models
from datetime import datetime
# Create your models here.


class User(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Admin(User):
    job_title = models.CharField(max_length=200)
    # date time to be changed
    hire_date = models.DateTimeField(default=datetime.now())


class Customer(User):
    phone = models.CharField(max_length=30)
    adress = models.CharField(max_length=200)


class Category(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name_en = models.CharField(max_length=200)
    name_ar = models.CharField(max_length=200)
    unit_price = models.DecimalField(max_digits=10)
    stock_quantity = models.DecimalField(max_digits=5)
    category = models.ManyToManyField(Category, on_delete=models.RESTRICT)


class Order(models.Model):
    create_date = models.DateTimeField(default=datetime.now())
    total_price = models.DecimalField()
    customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    # todo: status enum


class OrderDetails(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product_id = models.ManyToManyField(Product, on_delete=models.RESTRICT)
    unit_price = models.DecimalField(max_digits=6)
    ordered_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # todo: increase order counter dynamically
        pass
