from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from animal.models import Cat
from animal.serializer import CatSerializer


class CatService(APIView):
    """
    猫相关的类
    """
    def __init__(self):
        super().__init__()
        self.cat = Cat
        self.serializer = CatSerializer

    def get(self, request):
        """
        获取所有猫信息
        :param request:
        :return:
        """
        # 获取数据
        cats = self.cat.objects.all()
        # 序列化数据
        cat_serializer = self.serializer(cats, many=True)
        return Response(cat_serializer.data)

    def post(self, request):
        """
        存储数据
        :param request:
        :return:
        """
        cat_serializer = self.serializer(data=request.data)
        if cat_serializer.is_valid():
            cat_serializer.save()
            return Response('ok')
        return Response('error')

    def put(self, request):
        """
        更新数据
        :param request:
        :return:
        """
        data = request.data
        cat = self.cat.objects.filter(id=data.get('id')).first()

        if cat:
            print(data.get('color'))
            cat.color = data.get('color', cat.color)
            cat.weight = data.get('weight', cat.weight)
            cat.save()
            return Response('ok')
        return Response('error')
