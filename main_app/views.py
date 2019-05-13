from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Graph, Dev
from .serializers import GraphSerializer, DevSerializer
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import permissions



class GraphView(APIView):
    """
    GET: [{'graph_name':'', 'graph_content':'', 'graph_status':'', 'upper_limit':'', 'lower_limit':'', 'size':'',
           'graph_position':'', 'create_time'},
        ]

    POST:{'graph_name':'', 'graph_status':'', 'upper_limit':'', 'lower_limit':'', 'size':''},

    """

    def get(self, request):
        query_data = Graph.objects.all()  # 从数据库取出数据，query_set
        serializer = GraphSerializer(query_data, many=True)  # 将query_set序列化成Python数据类型
        # data = JSONRenderer().render(serializer.data)  # 将Python数据类型转成JSON
        # print(data)
        return Response(serializer.data)

    def post(self, request):
        """
        graph_conf 2|5|10000
        反序列化，将JSON形式数据转换为流的形式，然后将流数据转化为Python数据类型
        :param request:
        :return:
        """
        stream = BytesIO(request.body)  # 将JSON数据转换为流形式
        data = JSONParser().parse(stream)  # 解析流中的JSON数据并转换为Python数据结构
        serializer = GraphSerializer(data=data)
        if serializer.is_valid():  # 验证前台传过来的数据是否合法，在save前必须调用该方法
            serializer.save(**data)  # 根据是否存在instance实例来决定执行create方法或update方法，无执行create
        #  save方法可以选择传参或者不传参，不传参的话默认会从serializer实例化时传入的数据进行读取
        #  但是这样读取的话，非model定义的字段会被舍弃掉，所以如果需要传入非model定义的字段，需要在save方法传入data
            return 0

        #  print(serializer.errors)

    def patch(self, request):
        stream = BytesIO(request.body)
        data = JSONParser().parse(stream)
        serializer = GraphSerializer(data=data)
        serializer.instance = Graph.objects.get(id=data['id'])
        if serializer.is_valid():
            serializer.save(**data)
        return 0

    def delete(self, request):
        """
        RESTful默认界面的DELETE方法会将URL中的id传递给后台，如果没有使用URL传参的话，是不会传过来数据的
        自己传递JSON过来使用以下方法解析即可
        :param request:
        :return:
        """
        stream = BytesIO(request.body)
        data = JSONParser().parse(stream)
        g_id = data['id']
        obj = Graph.objects.get(id=g_id)
        obj.delete()
        return Response({"status": 0})

class DeViewset(viewsets.ModelViewSet):
    """
    ModelViewset继承了四个混类和一个泛类，自动会实现增删查改的方法
    viewset相当于是视图的集合，综合了多个方法
    """
    queryset = Dev.objects.all().order_by('id')
    serializer_class = DevSerializer
    lookup_field = 'id'  # 定义通过哪个参数来定位实例
    #permission_classes = (permissions.IsAdminUser,)  # 设置该视图的权限
    from g_conf.permissions import AdminPermissions
    permission_classes = (AdminPermissions, )