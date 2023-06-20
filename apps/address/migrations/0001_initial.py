# Generated by Django 4.2.2 on 2023-06-20 20:34

import apps.address.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Province",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(default="", max_length=32, verbose_name="Title"),
                ),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        default="None",
                        max_length=64,
                        verbose_name="Slug",
                    ),
                ),
            ],
            options={
                "verbose_name": "Province",
                "verbose_name_plural": "Provinces",
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(default="", max_length=32, verbose_name="Title"),
                ),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        default="None",
                        max_length=64,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "province",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="address.province",
                        verbose_name="Province",
                    ),
                ),
            ],
            options={
                "verbose_name": "City",
                "verbose_name_plural": "Cities",
            },
        ),
        migrations.CreateModel(
            name="Address",
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
                    "fullname",
                    models.CharField(
                        default="", max_length=32, verbose_name="Full name"
                    ),
                ),
                (
                    "mobile",
                    models.CharField(max_length=11, verbose_name="Mobile number"),
                ),
                ("address", models.TextField(max_length=256, verbose_name="Address")),
                (
                    "post_code",
                    models.CharField(
                        max_length=10,
                        unique=True,
                        validators=[apps.address.validators.arithmetic_numbers],
                        verbose_name="Postal_code",
                    ),
                ),
                ("active", models.BooleanField(default=False, verbose_name="Active")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Create time"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Update time"
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        max_length=32,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="address.city",
                        verbose_name="City",
                    ),
                ),
                (
                    "province",
                    models.ForeignKey(
                        max_length=32,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="address.province",
                        verbose_name="Province",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="address",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "User address",
                "verbose_name_plural": "User addresses",
            },
        ),
    ]
