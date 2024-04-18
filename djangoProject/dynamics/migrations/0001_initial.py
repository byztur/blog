# Generated by Django 4.2.7 on 2024-03-30 06:38

import DjangoUeditor.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'db_table': 'tag_lib',
            },
        ),
        migrations.CreateModel(
            name='Dynamic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('description', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='发布时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='dynamics/images', verbose_name='展报')),
                ('likeCount', models.IntegerField(default=0, verbose_name='点赞')),
                ('dislikeCount', models.IntegerField(default=0, verbose_name='踩')),
                ('commentCount', models.IntegerField(default=0, verbose_name='评论数')),
                ('classification', models.SmallIntegerField(choices=[(5, '日常'), (4, '娱乐'), (3, '政治'), (2, '社会'), (1, '体育'), (6, '测试')], verbose_name='分类')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发布人')),
            ],
            options={
                'verbose_name': '动态',
                'verbose_name_plural': '动态',
                'ordering': ['-publishDate'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('likeCount', models.IntegerField(default=0, verbose_name='点赞')),
                ('dislikeCount', models.IntegerField(default=0, verbose_name='踩')),
                ('dynamic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dynamics.dynamic')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'db_table': 'comment_lib',
            },
        ),
    ]