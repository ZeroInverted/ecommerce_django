# Generated by Django 4.2.4 on 2023-09-08 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0002_alter_admin_options_alter_customer_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admin",
            name="hire_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 8, 21, 28, 55, 72006)
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 8, 21, 28, 55, 72506)
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Delivered", "Delivered"),
                    ("Approved", "Approved"),
                    ("Declined", "Declined"),
                    ("Shipped", "Shipped"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]