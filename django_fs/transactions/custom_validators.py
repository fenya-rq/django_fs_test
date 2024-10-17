from decimal import Decimal
from django.core.exceptions import ValidationError
from django.core.validators import DecimalValidator


class PositiveDecimalValidator(DecimalValidator):
    """
    Кастомный валидатор, наследованный от `DecimalValidator`
    c реализацией дополнительных методов нужных проверок.
    """

    value_error: str = (
        "Невозможно выполнить операцию с {} значением. " "Введите сумму от 0.01"
    )

    def __call__(self, value: Decimal) -> None:
        """
        Вызывается для проверки переданного значения на соответствие условиям.

        Проверяет, что сумма является положительным значением и не равна нулю.
        Также выполняет встроенные проверки DecimalValidator, связанные с
        максимальным количеством цифр и десятичных знаков.

        :param value: Decimal: Проверяемое значение суммы.
        :raises ValidationError: Если сумма отрицательная или равна нулю.
        """
        super().__call__(value)
        self.check_for_negative(value)
        self.check_for_zero(value)

    def check_for_negative(self, value: Decimal) -> None:
        """
        Проверяет, что значение суммы не отрицательное.

        :param value: Decimal: Проверяемое значение суммы.
        :raises ValidationError: Если значение меньше нуля.
        """
        if value < Decimal("0"):
            raise ValidationError(self.value_error.format("отрицательным"))

    def check_for_zero(self, value: Decimal) -> None:
        """
        Проверяет, что значение суммы не равно нулю.

        :param value: Decimal: Проверяемое значение суммы.
        :raises ValidationError: Если значение равно нулю.
        """
        if value == Decimal("0"):
            raise ValidationError(self.value_error.format("нулевым"))
