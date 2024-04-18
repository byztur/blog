from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse

from dynamics import models
from user.models import UserInformationModel
from dynamics.models import Dynamic,Comment


# Create your views here.
# 获取最新动态
def get_new(request):
    res = Dynamic.objects.all().order_by('-publishDate')[:5]
    # print(res[0])
    # print(res[1:])
    return render(request,'dynamics/new_article.html',{'article':res[0],'nexts':res[1:]})


# 发布新动态
@login_required
def add_new(request):
    if request.method == "GET":
        context = {
            'class_choices' : models.class_choices,
        }
        return render(request, 'dynamics/add.html',context)

    if request.method == "POST":
        # 从请求中获取新动态的文本及图片
        title = request.POST.get('title')
        description = request.POST.get('description')
        photo = request.FILES.get('image')
        classification_id = request.POST.get('classification')
        # print(classification_id)
        # 创建数据库行
        Dynamic.objects.create(user=request.user, title=title, description=description, photo=photo, classification=classification_id)
        return redirect('/dynamics/new/')

    return render(request,'dynamics/add.html',{})

# 获取用户个人的所有动态
@login_required
def get_mynews(request):
    res = Dynamic.objects.filter(user=request.user).order_by('publishDate')[:10]
    return render(request, 'dynamics/my_news.html', {'res': res})

# 查看这个动态细节
def check(request, id):
    dynamic = Dynamic.objects.get(id=id)
    # print(dynamic.id)
    # 找到相关评论
    comment_lib = Comment.objects.filter(dynamic=dynamic)
    # print(comment_lib)
    author = dynamic.user
    return render(request, 'dynamics/check.html',{'dynamic': dynamic, 'author':author, 'comment_list':comment_lib})

# 删除动态
def delete(request, id):
    dynamic = Dynamic.objects.get(id=id)
    Dynamic.objects.get(id=id).delete()
    print("删除成功")
    return redirect('/dynamics/mynews/')

# 搜索动态
def search(request): # terms 搜索词
    # 错误信息
    err_msg = ""
    if request.method == "POST":
        terms = request.POST.get("search_res")
        dynamics = Dynamic.objects.filter(title__icontains=terms)
        if dynamics is None:
            print("没有数据")
            err_msg = "查找错误"
    else:
        pass
    # print(terms)
    # print(dynamics)
    print("搜索成功")
    # 把所有搜索结果传过去
    return render(request, 'dynamics/search.html',{'dynamics':dynamics})


# 按热度排序 实际上就是获取热度最高的动态
def getHot(request):
    res = Dynamic.objects.all().order_by('likeCount','commentCount','-dislikeCount')
    # print(res)
    return render(request,'dynamics/hot_article.html',{'article':res[0],'nexts':res[1:]})

# 按时间排序

# 查找各个栏目标签
def search_classification(request):
    res = []
    for i in range(1,len(models.class_choices)+1):
        res.append(Dynamic.objects.filter(classification=i).order_by('-publishDate')[:3])
    class_choices = models.class_choices
    # 返回给首页页面
    return render(request,"dynamics/dynamic_index.html",{'res':res,'class_choices':class_choices})
    # return HttpResponse("success")

# 点赞
def like(request):# 根据这个动态的id查到这个动态的数据，然后对点赞数进行更新
    id = request.POST.get("id")
    # print(data)
    dynamic = Dynamic.objects.get(id=id)
    lc = dynamic.likeCount
    # # 让点赞数量加1
    dynamic.likeCount = lc + 1
    dynamic.save()
    # 跳转更新到最新动态页面
    return HttpResponse(dynamic.likeCount)

# 前提条件是必须得进入这个详细界面 踩
def dislike(request):# 根据这个动态的id查到这个动态的数据，然后对点赞数进行更新
    id = request.POST.get("id")
    # print(data)
    dynamic = Dynamic.objects.get(id=id)
    dlc = dynamic.dislikeCount
    # # 让点赞数量加1
    dynamic.dislikeCount = dlc + 1
    dynamic.save()
    # 跳转更新到最新动态页面
    return HttpResponse(dynamic.dislikeCount)
# 增加评论
@login_required
def addComment(request,id):
    if request.method == "POST":
        # 获取评论
        comment = request.POST.get("comment")
        # 获取用户
        user = request.user
        # print(comment)
        # print(user)
        if comment is None:
            return HttpResponse("failed")
        comment = Comment.objects.create(user=user,description=comment)
        # print(comment)
        dynamic = Dynamic.objects.get(id=id)
        # print(dynamic)
        comment.dynamic = dynamic
        # print(dynamic.comment)
        dynamic.commentCount = dynamic.commentCount + 1
        # print(dynamic.commentCount)
        comment.save()
        dynamic.save()
    return redirect('/dynamics/check/' + str(id) + '/')

# 评论点踩
@login_required
def commentDis(request):
    if request.method == "POST":
        # 获取评论id
        comment_id = request.POST.get("id")
        # print(comment_id)
        # 查询评论
        comment = Comment.objects.get(id=comment_id)
        # print(comment.dislikeCount)
        comment.dislikeCount = comment.dislikeCount + 1
        # print(comment.dislikeCount)
        comment.save()
        # print(comment)
        # 获取动态id
        dynamic_id = request.POST.get("did")
        # print(dynamic_id)
        return HttpResponse(comment.dislikeCount)

# 评论点赞
@login_required
def commentLike(request):
    if request.method == "POST":
        # 获取评论id
        comment_id = request.POST.get("id")
        # print(comment_id)
        # 查询评论
        comment = Comment.objects.get(id=comment_id)
        # print(comment.dislikeCount)
        comment.likeCount = comment.likeCount + 1
        # print(comment.likeCount)
        comment.save()
        # print(comment)
        # 获取动态id
        dynamic_id = request.POST.get("did")
        # print(dynamic_id)
        return HttpResponse(comment.likeCount)