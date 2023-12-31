# Generated by Django 4.2.4 on 2023-09-11 03:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0012_alter_admin_hire_date_alter_order_create_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admin",
            name="hire_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 11, 6, 24, 50, 279654)
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 11, 6, 24, 50, 280654)
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Delivered", "Delivered"),
                    ("Shipped", "Shipped"),
                    ("Declined", "Declined"),
                    ("Pending", "Pending"),
                    ("Approved", "Approved"),
                ],
                max_length=20,
            ),
        ),
    ]
