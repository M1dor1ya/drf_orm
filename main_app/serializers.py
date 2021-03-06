# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 11:07
# @Author  : Zcs
# @File    : serializers.py
from rest_framework import serializers
from .models import Graph, Dev
import random


class GraphSerializer(serializers.ModelSerializer):

    class Meta:
        model = Graph
        fields = '__all__'
        read_only_fields = ['graph_name', 'graph_content', 'graph_conf', 'graph_position', 'create_time']
        #  read_only_fields选项，表示该字段只用作查询出结果，不需要用户传值
        #  如果未设置该字段，那么表示所有字段都需要从serializer那传值，如果未传is_valid函数会返回False

        #  extra_kwargs = {'id': {'write_only': True}}
        #  提供extra_kwargs的方式来为某个字段指定其关键字参数，而不需要去显示指定(id=serializers.IntegerField())

    @staticmethod
    def create_graph(gspace, gtime, num):
        buff = ()
        for i in range(num):
            ret1 = random.randrange(gspace[0], gspace[1] + 1)
            ret2 = random.randrange(gtime[0], gtime[1] + 1)
            buff += ((ret1, ret2),)
        return buff

    #  验证用户传到后台的数据是否合法
    # def validate(self, attrs):
    #     return attrs

    def create(self, validated_data):
        print(validated_data)
        validated_data['graph_conf'] = str(validated_data['lower_limit']) + '|' + \
                                       str(validated_data['upper_limit']) + '|' + str(validated_data['size'])
        validated_data['graph_position'] = 0
        validated_data['graph_content'] = str(self.create_graph([1,4], [validated_data['lower_limit'],
                                                                        validated_data['upper_limit']],10))
        kwargs = {
            'graph_name': validated_data.get('graph_name'),
            'graph_content': validated_data.get('graph_content'),
            'graph_status': validated_data.get('graph_status'),
            'graph_conf': validated_data.get('graph_conf'),
            'graph_position': validated_data.get('graph_position'),
        }
        instance = Graph.objects.create(**kwargs)
        return instance

    def update(self, instance, validated_data):
        #  只允许更新graph_status参数
        instance.graph_status = validated_data['graph_status']
        instance.save()
        return instance

class DevSerializer(serializers.ModelSerializer):
    dev_user_name = serializers.ReadOnlyField()
    is_superuser = serializers.SerializerMethodField()

    class Meta:
        model = Dev
        fields = '__all__'

    @staticmethod
    def get_is_superuser(obj):
        return obj.dev_user.is_superuser

