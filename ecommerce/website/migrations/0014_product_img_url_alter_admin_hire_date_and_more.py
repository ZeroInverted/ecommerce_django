# Generated by Django 4.2.4 on 2023-09-11 03:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0013_alter_admin_hire_date_alter_order_create_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="img_url",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="admin",
            name="hire_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 11, 6, 29, 23, 796891)
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 11, 6, 29, 23, 797394)
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Shipped", "Shipped"),
                    ("Approved", "Approved"),
                    ("Declined", "Declined"),
                    ("Delivered", "Delivered"),
                ],
                max_length=20,
            ),
        ),
    ]
