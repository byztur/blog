"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from dynamics import views

app_name = 'dynamics'

urlpatterns = [
    path('new/', views.get_new), # 获取最新动态
    path('add/', views.add_new), # 添加动态
    path('mynews/', views.get_mynews), # 获取自己的最新动态
    path('check/<int:id>/', views.check), # 查看一篇动态
    path('delete/<int:id>/', views.delete), # 删除动态
    path('search/',views.search), # 搜索动态
    path('index/',views.search_classification), # 首页
    path('like/',csrf_exempt(views.like)),# 点赞
    path('dislike/',csrf_exempt(views.dislike)), # 踩
    path('comment/add/<int:id>/',views.addComment), # 添加评论
    path('comment/like/',csrf_exempt(views.commentLike)), # 评论点赞
    path('comment/dislike/',csrf_exempt(views.commentDis)),# 评论踩
    path('hot/', views.getHot)# 按热度排行
]
