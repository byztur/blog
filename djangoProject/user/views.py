from django.contrib import auth
from django.shortcuts import render, HttpResponse, redirect
from user import models
import re


# Create your views here.
# 注册页面
def register(request):
    # 错误信息
    err_msg = {}
    # 用户提交的信息
    user_info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        user_info = {'username': username, 'password1': password1, 'password2': password2}
        # 验证用户名
        if len(username) <= 3 or len(username) > 10:
            err_msg['username'] = "用户名长度不符合要求，应大于3小于等于10！"
        elif not re.match("^[a-zA-Z0-9_]+$", username):
            err_msg['username'] = "用户名含有无效字符，只能由大小写字符、数字及下划线构成！"
        else:
            res = models.UserInformationModel.objects.filter(username=username)
            if len(res) > 0:
                # 用户名重名存在
                err_msg['username'] = "用户名已经存在！"
            else:
                # 用户名有效
                # 检验密码
                if len(password1) < 6 or len(password1) > 16:
                    err_msg['password1'] = "密码长度无效，应该大于6小于16！"
                elif password1 != password2:
                    # 两次密码输入不同
                    err_msg['password2'] = "两次输入的密码不一致！"
                else:
                    # 创建用户数据
                    models.UserInformationModel.objects.create_user(username=username, password=password1)
                    return redirect("/userinfo/login/")
    # get方式
    else:
        pass

    return render(request, "../templates/user/register.html",
                  {'user_info': user_info, 'err_msg': err_msg})


def login(request):
    # 错误信息
    err_msg = ""
    # 用户提交的信息
    user_info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_info = {'username': username, 'password': password}
        res = auth.authenticate(username=username,password=password)
        if res is None:
            # 用户名密码错误
            print("用户没找到！")
            err_msg = "用户名或密码错误！"
        else:
            # 用户名正确
            auth.login(request, res)
            # return redirect("/depart/list/")
            return redirect("/userinfo/edit/")

        # get方式
    else:
        pass

    return render(request, "../templates/user/login.html",
                  {'user_info': user_info, 'err_msg': err_msg})

from django.contrib.auth.decorators import login_required
@login_required # 必须登陆后才能访问该视图
def logout(request):
    auth.logout(request)
    return redirect('/userinfo/login/')

# 编辑个人信息
@login_required
def edit(request):
    user = request.user
    if request.method == "POST":
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.nike_name = request.POST.get("nike_name")
        user.birthday = request.POST.get("birthday")
        user.gender = request.POST.get("gender")
        user.describe = request.POST.get("describe")
        image = request.FILES.get('image')
        # print(image)
        if image:
            print(image)
            user.image = image
        else:
            print("没有提交图片")
        user.save()

        return render(request, 'user/edit.html', {'user':
                                                      {'first_name': user.first_name,
                                                       'last_name': user.last_name,
                                                       'nike_name': user.nike_name,
                                                       'birthday': user.birthday,
                                                       'gender': user.gender,
                                                       'describe': user.describe,
                                                       'image': user.image}})
    else:
        userinfo = {'first_name':user.first_name,
            'last_name':user.last_name,
            'nike_name':user.nike_name,
            'gender':user.gender,
            'describe':user.describe,
            'image':user.image}
        if user.birthday is None:
            userinfo['birthday'] = None
        elif type(user.birthday) == str:
            userinfo['birthday'] = user.birthday
        else:
            userinfo['birthday'] = user.birthday.strftime("%Y-%m-%d")
        return render(request, 'user/edit.html', {'user':userinfo})
