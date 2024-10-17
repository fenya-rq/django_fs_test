#!/usr/bin/env pytnon3
# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet

from .models import ClientUser
from .serializers import ClientUserSerializer


class ClientUserViewSet(ModelViewSet):
    """
    Представление для управления пользователями (ClientUser).

    Обеспечивает CRUD операции:
    - Получение списка пользователей
    - Создание нового пользователя
    - Обновление существующего пользователя
    - Удаление пользователя
    """

    http_method_names = ["get", "post", "put", "delete"]
    queryset = ClientUser.objects.all().order_by("id")
    serializer_class = ClientUserSerializer
