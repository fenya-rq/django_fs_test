#!/usr/bin/env pytnon3
# -*- coding: utf-8 -*-
from django.urls import path, include

from .routers import router

urlpatterns = [path("", include(router.urls))]
