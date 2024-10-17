#!/usr/bin/env pytnon3
# -*- coding: utf-8 -*-
from django.db import models
from . import PositiveDecimalValidator


class UserTransactions(models.Model):
    """
    Модель для хранения информации о финансовых транзакциях пользователя.

    Атрибуты:
    ----------
    user : ForeignKey
        Ссылка на модель клиента, к которому привязана транзакция.
    amount : DecimalField
        Сумма транзакции с максимальной точностью в 10 цифр, включая 2
        десятичных знака. Проверяется на положительное значение с
        использованием кастомного валидатора.
    operation_dt : DateTimeField
        Дата и время совершения транзакции, автоматически заполняется
        при создании записи.
    change_dt : DateTimeField
        Дата и время последнего изменения записи, автоматически обновляется
        при каждом изменении.
    kind : CharField
        Вид операции, например, "Расход" или "Доход".
    category : CharField
        Категория операции, описывающая назначение транзакции, например,
        "Зачисление ЗП" или "Покупка".
    """

    user = models.ForeignKey(
        to="users.ClientUser", on_delete=models.CASCADE, verbose_name="Клиент"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=(PositiveDecimalValidator(max_digits=10, decimal_places=2),),
        verbose_name="Сумма",
    )
    operation_dt = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата совершения операции"
    )
    change_dt = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    kind = models.CharField(max_length=6, verbose_name="Вид операции")
    category = models.CharField(max_length=50, verbose_name="Категория")

    def __str__(self) -> str:
        return (
            f"{self.operation_dt}\nТранзакция c ID {self.id} "
            f"на сумму {self.amount} успешно выполнена."
            f"\nТип транзакции - {self.kind}\nКлиент {self.user} с ID {self.user.id}."
        )

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ) -> None:
        self.full_clean()
        super().save()
