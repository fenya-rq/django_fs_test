from django.core.validators import validate_email
from django.db import models


class ClientUser(models.Model):
    """
    Модель для хранения информации о клиенте.

    Атрибуты:
    ----------
    name : CharField
        Имя клиента с максимальной длиной 35 символов.
    surname : CharField
        Фамилия клиента с максимальной длиной 50 символов.
    email : EmailField
        Электронная почта клиента, проверяется встроенным валидатором
        на корректность email-адреса. Поле уникально, т.е. не может быть
        дублирующих записей с одинаковым email.
    registration_dt : DateTimeField
        Дата и время регистрации клиента. Автоматически заполняется при
        создании записи.
    """

    name = models.CharField(max_length=35, verbose_name="Имя клиента")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(
        max_length=100,
        validators=(validate_email,),
        verbose_name="Электронная почта",
        unique=True,
    )
    registration_dt = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата регистрации"
    )

    def __str__(self) -> str:
        return f"{self.name}"

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
