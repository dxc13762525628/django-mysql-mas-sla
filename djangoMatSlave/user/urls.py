#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/9/23 10:01 
# @Author : dxc
# @File : urls.py
from django.urls import path

from user.views import *

urlpatterns = [
    path('api/user/', UserService.as_view()),
]
