#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/9/23 11:24 
# @Author : dxc
# @File : serializer.py
from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    用户表的序列化器
    """

    class Meta:
        model = User
        fields = '__all__'
