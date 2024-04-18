# Generated by Django 4.2.7 on 2024-03-23 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_alter_userinfo_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(2, '女'), (1, '男')], verbose_name='性别'),
        ),
    ]