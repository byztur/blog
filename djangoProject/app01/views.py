from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01 import models


# Create your views here.
def depart_list(request):
    """部门列表"""

    # 去数据库中获取所有的部门列表
    queryset = models.Department.objects.all()

    return render(request, 'depart_list.html', {'queryset': queryset})


def depart_add(request):
    """添加部门"""
    if request.method == "GET":
        return render(request, 'depart_add.html')
    # 获取post提交过来的数据
    title = request.POST.get("title")

    # 保存到数据库
    models.Department.objects.create(title=title)

    # 重定向回列表页面
    return redirect("/depart/list/")


def depart_delete(request):
    """删除部门"""
    nid = request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()
    # 重定向回列表页面
    return redirect("/depart/list/")


def depart_edit(request, nid):
    """编辑部门"""
    if request.method == "GET":
    # 根据nid，获取数据
        row_object = models.Department.objects.filter(id=nid).first()
        # print(row_object.id, row_object.title)
        return render(request, 'depart_edit.html', {"row_object": row_object})
    title = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=title)
    # 重定向回列表页面
    return redirect("/depart/list/")


def user_list(request):
    """用户管理"""

    # 获取所有用户
    queryset = models.UserInfo.objects.all()
    # for obj in queryset:
        # 关联性搜索查询
        # obj.depart # 根据id自动去关联的表中获取一行数据
        # obj.depart.title

    return render(request, 'user_list.html',{"queryset":queryset})


def user_add(request):
    """添加用户"""
    if request.method == "GET":
        context = {
            'gender_choices' : models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all(),
        }
        return render(request, 'user_add.html',context)

    # 获取用户提交的数据
    user = request.POST.get("username")
    pwd = request.POST.get("password")
    age = request.POST.get("age")
    account = request.POST.get("account")
    ctime = request.POST.get("ctime")
    gender_id = request.POST.get("gender")
    depart_id = request.POST.get("depart")

    # 添加到数据库中
    models.UserInfo.objects.create(name=user,password=pwd,age=age,
                                   account=account,create_time=ctime,
                                   gender=gender_id,depart_id=depart_id)

    # 返回用户列表页面
    return redirect("/user/list/")


#############################################
from django import forms
class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name","password","age","account","create_time","depart","gender"]
        # widgets = {
        #     "name":forms.TextInput(attrs={"class":"form-control"})
        #     "password":forms.PasswordInput(attrs={"class":"form-control"})
        # }
    def __init__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)

        for name,field in self.fields.items():
            print(name, field)
            field.widget.attrs = {"class": "form-control"}

def user_model_form_add(request):
    """添加用户 modelform"""
    form = UserModelForm()
    return render(request,'user_model_form_add.html',{"form":form})

#################以下均为测试############################
def articles_test(request):
    return render(request,'articles_test.html')

def articles_demo(request,year):
    # print(year)
    # request.user.username
    # request.user.password
    if year is None:
        print("年份为空")
    return render(request,'articles_demo.html')

    # return HttpResponse("hello")
    # 不能return True
    # return True