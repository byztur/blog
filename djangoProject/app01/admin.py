from django.contrib import admin

from app01.models import Department, UserInfo

# Register your models here.
# 管理员后台
admin.site.register(Department)
admin.site.register(UserInfo)