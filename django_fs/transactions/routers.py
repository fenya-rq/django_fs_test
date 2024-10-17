#!/usr/bin/env pytnon3
# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter

from .views import UserTransactionsViewSet

router = DefaultRouter()

router.register("api/v1/transactions", UserTransactionsViewSet)
