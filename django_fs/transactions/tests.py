#!/usr/bin/env pytnon3
# -*- coding: utf-8 -*-
from decimal import Decimal

import pytest
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from users.models import ClientUser
from .models import UserTransactions
from .custom_validators import PositiveDecimalValidator


@pytest.mark.django_db
class TestClientsTransactions:
    """
    Тестирование всех CRUD операций и валидации данных
    в модели `UserTransactions`.
    """

    @pytest.fixture(autouse=True)
    def setup_fixtures(self, load_fixture):
        """
        Автоматически загружает фикстуры `clients` и `transactions`
        перед каждым тестом.

        :param load_fixture: callable: Фикстура для загрузки
         данных из JSON-файлов фикстур в базу данных.
        """
        load_fixture("clients")
        load_fixture("transactions")

    def test_create_transaction_ok(self):
        """
        Проверка получения транзакции по её первичному ключу.
        Убедитесь, что транзакция с определенным `pk` загружается
        корректно, и сумма совпадает.
        """
        user = ClientUser.objects.get(pk=1)
        transaction = UserTransactions(
            user=user,
            amount=100,
            operation_dt="2024-10-10T19:14:23+03:00",
            change_dt="2024-10-10T19:14:23+03:00",
            kind="Расход",
            category="Зачисление ЗП",
        )
        transaction.save()
        assert isinstance(transaction, UserTransactions)

    def test_get_transaction_ok(self):
        """
        Проверка получения транзакции по её первичному ключу.
        Убедитесь, что транзакция с определенным `pk` загружается
        корректно, и сумма совпадает.
        """
        transaction = UserTransactions.objects.get(pk=1)
        assert transaction.amount == 1400.25

    def test_update_transaction_ok(self):
        """
        Проверка успешного обновления полей транзакции.
        Убедитесь, что можно изменить сумму и категорию
        транзакции, и они сохраняются правильно.
        """
        transaction = UserTransactions.objects.get(pk=1)
        assert transaction.amount == 1400.25
        assert transaction.category == "Зачисление ЗП"

        transaction.category = "Перевод физ. лицу"
        transaction.amount = 1200
        transaction.save()
        transaction = UserTransactions.objects.get(pk=1)
        assert transaction.amount == 1200
        assert transaction.category == "Перевод физ. лицу"

    def test_delete_transaction_ok(self):
        """
        Проверка успешного удаления транзакции.
        Убедитесь, что транзакция с определенным `pk`
        удаляется без ошибок.
        """
        assert UserTransactions.objects.get(pk=1).delete()

    def test_delete_transaction_error(self):
        """
        Проверка ошибки при удалении несуществующей транзакции.
        Убедитесь, что при попытке удаления транзакции, которая
        не существует, возникает ошибка `ObjectDoesNotExist`.
        """
        with pytest.raises(ObjectDoesNotExist):
            UserTransactions.objects.get(pk=5).delete()

    @pytest.mark.parametrize(
        "expected",
        (
            "2024-10-07 12:24:46+00:00\nТранзакция c ID 1 на сумму 1400.25 успешно выполнена."
            "\nТип транзакции - Приход\nКлиент Иван с ID 1.",
        ),
    )
    def test_str_representing_ok(self, expected):
        """
        Проверка строкового представления транзакции.
        Сравнивает результат метода `__str__` объекта транзакции с
        ожидаемым результатом.
        """
        transaction = UserTransactions.objects.get(pk=1)
        assert str(transaction) == expected


@pytest.mark.parametrize("validator", (PositiveDecimalValidator(10, 2),))
class TestCustomValidator:
    """
    Тесты для проверки пользовательского валидатора
    PositiveDecimalValidator.
    """

    def test_decimal_ok(self, validator):
        """
        Проверка валидации для положительного десятичного числа.
        Убедитесь, что валидатор пропускает корректные данные.
        """
        positive_decimal = Decimal("13.64")
        validator(positive_decimal)

    def test_decimal_zero_error(self, validator):
        """
        Проверка ошибки валидации для нулевого значения.
        Убедитесь, что валидатор вызывает ошибку для значения 0.
        """
        zero_decimal = Decimal(0)
        with pytest.raises(ValidationError):
            validator(zero_decimal)

    def test_decimal_negative_error(self, validator):
        """
        Проверка ошибки валидации для отрицательного значения.
        Убедитесь, что валидатор вызывает ошибку для
        отрицательного числа.
        """
        negative_decimal = Decimal("-13.64")
        with pytest.raises(ValidationError):
            validator(negative_decimal)
