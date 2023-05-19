# Generated by Django 4.2 on 2023-05-18 20:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_rename_is_success_order_is_paid_order_address_info_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="delivery_type",
            field=models.CharField(
                choices=[("NO", "Normal"), ("QU", "Quick")],
                default=("NO", "Normal"),
                max_length=32,
                verbose_name="Delivery type",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="payment_method",
            field=models.CharField(
                choices=[("BA", "Bank"), ("DD", "Didipay")],
                default=("NO", "Normal"),
                max_length=32,
                verbose_name="Payment method",
            ),
        ),
    ]
