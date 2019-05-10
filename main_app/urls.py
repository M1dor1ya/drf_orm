# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 11:34
# @Author  : Zcs
# @File    : urls.py.py
from django.urls import path
from . import views

urlpatterns = [
    path('graph/', views.GraphView.as_view()),

]