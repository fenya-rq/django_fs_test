#!/usr/bin/env pytnon3
# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet

from .models import UserTransactions
from .serializers import UserTransactionsSerializer


class UserTransactionsViewSet(ModelViewSet):
    """
    Представление для управления транзакциями пользователей (UserTransactions).

    Обеспечивает CRUD операции:
    - Получение списка транзакций
    - Создание новой транзакции
    - Обновление существующей транзакции
    - Удаление транзакции
    """

    http_method_names = ["get", "post", "put", "delete"]
    queryset = UserTransactions.objects.all().order_by("operation_dt")
    serializer_class = UserTransactionsSerializer
