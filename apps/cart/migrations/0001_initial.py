# Generated by Django 4.2.2 on 2023-06-20 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "total_price",
                    models.IntegerField(default=0, verbose_name="Total price"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cart",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Shopping cart",
                "verbose_name_plural": "Shopping Carts",
            },
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "idkc",
                    models.BigIntegerField(
                        default=0, editable=False, verbose_name="idkc"
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(default=0, verbose_name="Quantity"),
                ),
                (
                    "base_total_price",
                    models.IntegerField(
                        default=0, editable=False, verbose_name="Base total price"
                    ),
                ),
                (
                    "total_price",
                    models.IntegerField(
                        default=0, editable=False, verbose_name="Total price"
                    ),
                ),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cart_item",
                        to="cart.cart",
                        verbose_name="Cart items",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="cart_item",
                        to="product.productcustom",
                        verbose_name="Product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cart item",
                "verbose_name_plural": "Cart items",
            },
        ),
    ]