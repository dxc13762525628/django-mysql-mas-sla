#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/9/23 14:33 
# @Author : dxc
# @File : urls.py
from django.urls import path, include

from animal.views import CatService

urlpatterns = [
    path('api/cat/', CatService.as_view()),
]
