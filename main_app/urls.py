# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 11:34
# @Author  : Zcs
# @File    : urls.py.py
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


# router = routers.DefaultRouter()
# router.register('dev', views.DeViewset)  # 为viewset注册路由
dev_list = views.DeViewset.as_view({
    'get': 'list',
    'post': 'create'
})
dev_detail = views.DeViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    #path('', include(router.urls)),
    path('graph/', views.GraphView.as_view()),
    path('devs/', dev_list),
    path('devs/<int:id>/', dev_detail)
])