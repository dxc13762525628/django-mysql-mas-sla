from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
import random

from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializer import UserSerializer


class UserService(APIView):
    """
    用户相关
    """

    def __init__(self):
        super().__init__()
        self.user = User
        self.serializer = UserSerializer

    def get(self, request):
        """
        获取所有用户信息
        :param request:
        :return:
        """
        # 获取数据
        users = self.user.objects.all()
        # 序列化数据
        user_serializer = self.serializer(users, many=True)
        return Response(user_serializer.data)

    def post(self, request):
        """
        存储数据
        :param request:
        :return:
        """
        user_serializer = self.serializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response('ok')
        return Response('error')

    def put(self, request):
        """
        更新数据
        :param request:
        :return:
        """
        data = request.data
        user = User.objects.filter(id=data.get('id')).first()
        if user:
            user.name = data.get('name', user.name)
            user.age = data.get('age', user.age)
            user.save()
            return Response('ok')
        return Response('error')
