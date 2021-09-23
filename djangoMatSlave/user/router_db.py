#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/9/23 14:14 
# @Author : dxc
# @File : router_db.py


class Router:
    """
    读操作用slave库
    写操作用default
    """

    def db_for_read(self, model, **kwargs):
        """
        user读用主表
        cat读从表
        """
        app = model._meta.app_label
        if app == 'user':
            print("user读数据用主表")
            return 'default'
        print("cat使用从表数据库读数据")
        return 'slave'

    def db_for_write(self, model, **kwargs):
        print("使用主表数据库写数据")
        return 'default'
