# Generated by Django 4.2.4 on 2023-09-10 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "website",
            "0009_remove_orderdetails_unit_price_alter_admin_hire_date_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="admin",
            name="hire_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 11, 0, 18, 54, 760976)
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 11, 0, 18, 54, 761476)
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Shipped", "Shipped"),
                    ("Pending", "Pending"),
                    ("Delivered", "Delivered"),
                    ("Approved", "Approved"),
                    ("Declined", "Declined"),
                ],
                max_length=20,
            ),
        ),
    ]