# Generated by Django 4.2.7 on 2024-03-30 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0013_alter_userinfo_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别'),
        ),
    ]