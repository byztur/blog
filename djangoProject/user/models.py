from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
import datetime
class UserInformationModel(AbstractUser):
    nike_name = models.CharField(max_length=50, verbose_name=u"昵称", default='')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="female")
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=200, null=True)
    describe = models.CharField(max_length=500, default=' ', verbose_name=u'个性签名')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
