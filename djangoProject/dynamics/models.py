from django.db import models
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone
from user.models import UserInformationModel
# Create your models here.

class_choices = {
        (1,"体育"),
        (2,"社会"),
        (3,"政治"),
        (4,"娱乐"),
        (5,"日常"),
        (6,"测试")
    }
# 动态
class Dynamic(models.Model):
    user = models.ForeignKey(to=UserInformationModel, on_delete=models.CASCADE, verbose_name="发布人", default=1)
    title = models.CharField(max_length=50, verbose_name='标题')
    description = UEditorField(u'内容',
                               default='',
                               width=1000,
                               height=300,
                               imagePath='dynamics/images/',
                               filePath='dynamics/files/')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量', default=0)
    photo = models.ImageField(upload_to='dynamics/images',
                              blank=True,
                              null=True,
                              verbose_name='展报')
    likeCount = models.IntegerField(default=0, verbose_name='点赞')
    dislikeCount = models.IntegerField(default=0, verbose_name='踩')
    commentCount = models.IntegerField(default=0, verbose_name='评论数')

    classification = models.SmallIntegerField(verbose_name="分类", choices=class_choices)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishDate']
        verbose_name = "动态"
        verbose_name_plural = verbose_name

# 评论
class Comment(models.Model):
    user = models.ForeignKey(UserInformationModel, null=True,on_delete=models.CASCADE)
    description = UEditorField(u'内容',
                               default='',
                               width=1000,
                               height=300,
                               imagePath='dynamics/comment/images/',
                               filePath='dynamics/comment/files/')
    likeCount = models.IntegerField(default=0, verbose_name='点赞')
    dislikeCount = models.IntegerField(default=0, verbose_name='踩')
    dynamic = models.ForeignKey(Dynamic,null=True,on_delete=models.CASCADE)

    class Meta:
        db_table = "comment_lib"
        verbose_name = "评论"
        verbose_name_plural = "评论"
# 标签
class Tag(models.Model):
    content = models.CharField(max_length=50, verbose_name='标签')
    classification = models.SmallIntegerField(verbose_name="分类", choices=class_choices)
    dynamic = models.ManyToManyField(to='Dynamic')


    class Meta:
        db_table = "tag_lib"
        verbose_name = "标签"
        verbose_name_plural = "标签"

# 我的讨论
# class Discussion(models.Model):
#     user = models.ForeignKey(UserInformationModel,null=True,on_delete=models.SET_NULL())
#     likes = models.PositiveIntegerField(verbose_name="喜欢", default=0, editable=False)
#     class Meta:
#         verbose_name_plural = "Discussion"