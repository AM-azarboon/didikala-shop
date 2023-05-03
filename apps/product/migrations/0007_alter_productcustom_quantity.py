# Generated by Django 4.2 on 2023-05-02 21:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0006_rename_counts_productcustom_quantity_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productcustom",
            name="quantity",
            field=models.PositiveIntegerField(default=0, verbose_name="Quantity"),
        ),
    ]