from django.db import models


class User(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=32, default='', verbose_name="名字")
    age = models.IntegerField(default=0, verbose_name="年龄")
