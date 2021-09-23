from django.db import models


class Cat(models.Model):
    color = models.CharField(max_length=32, default="")
    weight = models.CharField(max_length=32, default="")
