# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 10:27
# @Author  : Zcs
# @File    : permissions.py
from rest_framework import permissions
"""
三个角色：      普通用户  管理员
is_superuser：    0       1
"""

class AdminPermissions(permissions.IsAuthenticated):

    """
    此方法为设置是否具有具体对象的权限
    """
    def has_object_permission(self, request, view, obj):
        pass