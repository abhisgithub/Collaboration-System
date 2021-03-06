# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-24 07:29
from __future__ import unicode_literals

import BasicArticle.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to=BasicArticle.models.get_file_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_on', models.DateTimeField(null=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_author', to=settings.AUTH_USER_MODEL)),
                ('published_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_publisher', to=settings.AUTH_USER_MODEL)),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articleworkflow', to='workflow.States')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleViewLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=40)),
                ('session', models.CharField(max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articleviews', to='BasicArticle.Articles')),
            ],
        ),
    ]
