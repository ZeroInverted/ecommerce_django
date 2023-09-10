from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    is_staff = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Use email as a username
        if self.email:
            self.username = self.email
         # Split the full_name into first_name and last_name
        if self.full_name:
            names = self.full_name.split()
            if len(names) > 1:
                self.first_name = names[0]
                self.last_name = ' '.join(names[1:])
            else:
                # If there's only one name, set it as the first_name
                self.first_name = self.full_name
                self.last_name = ''
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Admin(User):
    job_title = models.CharField(max_length=200)
    hire_date = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"


class Customer(User):
    phone = models.CharField(max_length=30)
    adress = models.TextField()

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    name_en = models.CharField(max_length=200)
    name_ar = models.CharField(max_length=200)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.RESTRICT)
    # Use pillow to process images
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name_en

    # Check if an image exists, if so, return its URL, if it doesn't return an empty url.
    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Order(models.Model):
    create_date = models.DateTimeField(default=datetime.now())
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    status_choices = {
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered')
    }
    status = models.CharField(max_length=20, choices=status_choices)

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderDetails(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product_id = models.ForeignKey(Product, on_delete=models.RESTRICT)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_count = models.PositiveIntegerField()

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = "Order Detail"
        verbose_name_plural = "Orders Details"
