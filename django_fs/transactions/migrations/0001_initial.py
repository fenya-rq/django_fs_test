# Generated by Django 5.1.2 on 2024-10-11 14:34

import django.db.models.deletion
import transactions.custom_validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserTransactions",
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
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[
                            transactions.custom_validators.PositiveDecimalValidator(
                                decimal_places=2, max_digits=10
                            )
                        ],
                        verbose_name="Сумма",
                    ),
                ),
                (
                    "operation_dt",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата совершения операции"
                    ),
                ),
                (
                    "change_dt",
                    models.DateTimeField(auto_now=True, verbose_name="Дата изменения"),
                ),
                ("kind", models.CharField(max_length=6, verbose_name="Вид операции")),
                ("category", models.CharField(max_length=50, verbose_name="Категория")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.clientuser",
                        verbose_name="Клиент",
                    ),
                ),
            ],
        ),
    ]
