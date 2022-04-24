# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),    # 第二个实参制定了要调用的视图函数，第三个实参将URL模式名称指定为index，让我们能够在代码的其他地方使用它
    path('index/', views.index),
    path('add_mock/', views.add_mock),
    path('show_mock/', views.show_mock)
]