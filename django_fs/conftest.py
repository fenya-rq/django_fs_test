from typing import Callable

import pytest

from django.core.management import call_command


@pytest.fixture
def load_fixture(db) -> Callable[[str], None]:
    """
    Фикстура для загрузки JSON фиктуры в базу данных.

    :param db: *pytest фикстура*: Обеспечивает взаимодействие теста
     с базой данных.
    :return: Callable: Функция для загрузки фиктуры по имени.
    """

    def _load_fixture(file_name: str) -> None:
        """
        Загрузить конкретный файл фиктуры в тестовую базу данных.

        :param file_name: str: Имя файла фиктуры (без '.json' расширения).
        """
        call_command("loaddata", f"fixtures/{file_name}.json")

    return _load_fixture
