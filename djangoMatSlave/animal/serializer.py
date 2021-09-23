#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/9/23 14:47 
# @Author : dxc
# @File : serializer.py
from rest_framework import serializers

from animal.models import Cat


class CatSerializer(serializers.ModelSerializer):
    """
    猫相关
    """
    class Meta:
        model = Cat
        fields = '__all__'

