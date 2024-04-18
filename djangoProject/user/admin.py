from django.contrib import admin
from .models import UserInformationModel
# root123456密码
# Register your models here.
class AdminUserInformationModel(admin.ModelAdmin):
    list_display = ('username', 'nike_name')

admin.site.register(UserInformationModel,AdminUserInformationModel)