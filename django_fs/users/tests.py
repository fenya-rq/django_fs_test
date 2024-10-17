#!/usr/bin/env pytnon3
# -*- coding: utf-8 -*-
import pytest
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from .models import ClientUser


@pytest.mark.django_db
class TestClientsModel:
    """
    Тестирование всех CRUD операций и валидации данных.
    """

    @pytest.fixture(autouse=True)
    def setup_fixtures(self, load_fixture):
        """
        Автоматически загружает фикстуру 'clients' перед каждым тестом.

        :param load_fixture: Callable: Функция для загрузки фиктуры.
        """
        load_fixture("clients")

    def test_create_user_ok(self):
        """
        Тестирование успешного создания пользователя.
        """
        user = ClientUser(name="Иванов", surname="Петр", email="example@gmail.com")
        user.save()
        assert isinstance(user, ClientUser)

    def test_create_existing_email_error(self):
        """
        Тестирование ошибки создания пользователя с существующим email.
        """
        user = ClientUser(name="Даниил", surname="Мазепов", email="ivan@gmail.com")
        with pytest.raises(ValidationError):
            user.save()

    def test_get_user_ok(self):
        """
        Тестирование успешного получения пользователя по первичному ключу.
        """
        user = ClientUser.objects.get(pk=1)
        assert isinstance(user, ClientUser)
        assert user.name == "Иван"

    def test_update_user_ok(self):
        """
        Тестирование успешного обновления данных пользователя.
        """
        user = ClientUser.objects.get(pk=1)
        assert user.name == "Иван"
        user.name = "Алексей"
        user.save()
        user = ClientUser.objects.get(pk=1)
        assert user.name == "Алексей"

    def test_delete_user_ok(self):
        """
        Тестирование успешного удаления пользователя.
        """
        assert ClientUser.objects.get(pk=1).delete()

    def test_delete_user_error(self):
        """
        Тестирование ошибки удаления несуществующего пользователя.
        """
        with pytest.raises(ObjectDoesNotExist):
            ClientUser.objects.get(pk=5).delete()
