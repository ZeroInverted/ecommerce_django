# Generated by Django 4.2.4 on 2023-09-10 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0008_alter_admin_hire_date_alter_order_create_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderdetails",
            name="unit_price",
        ),
        migrations.AlterField(
            model_name="admin",
            name="hire_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 11, 0, 11, 59, 956120)
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 11, 0, 11, 59, 957120)
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Delivered", "Delivered"),
                    ("Shipped", "Shipped"),
                    ("Approved", "Approved"),
                    ("Declined", "Declined"),
                    ("Pending", "Pending"),
                ],
                max_length=20,
            ),
        ),
    ]