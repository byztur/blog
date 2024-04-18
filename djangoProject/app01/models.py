from django.db import models

# Create your models here.
class Department(models.Model):
    """ 部门表 """
    # id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="部门名", max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        db_table="app01_department"
        verbose_name = "部门表"
        verbose_name_plural = verbose_name


class UserInfo(models.Model):
    """ 员工表 """
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")
    # DateTimeField 合并日期和时间
    # DateField 日期
    # TimeField 时间

    depart = models.ForeignKey(verbose_name="所属部门",to="Department", to_field="id", on_delete=models.CASCADE)

    # 在django中做的约束
    gender_choices = {
        (1, "男"),
        (2, "女"),
    }
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)

    class Meta:
        db_table = "app01_userinfo"
        verbose_name = "用户表"
        verbose_name_plural = verbose_name


