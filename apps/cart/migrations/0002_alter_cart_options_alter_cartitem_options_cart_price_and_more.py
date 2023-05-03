# Generated by Django 4.2 on 2023-05-02 22:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cart",
            options={
                "verbose_name": "Shopping cart",
                "verbose_name_plural": "Shopping Carts",
            },
        ),
        migrations.AlterModelOptions(
            name="cartitem",
            options={"verbose_name": "Cart item", "verbose_name_plural": "Cart items"},
        ),
        migrations.AddField(
            model_name="cart",
            name="price",
            field=models.PositiveIntegerField(default=0, verbose_name="Total price"),
        ),
        migrations.AddField(
            model_name="cartitem",
            name="quantity",
            field=models.PositiveIntegerField(default=1, verbose_name="Quantity"),
        ),
        migrations.AddField(
            model_name="cartitem",
            name="total_price",
            field=models.PositiveIntegerField(default=0, verbose_name="Total price"),
        ),
    ]
