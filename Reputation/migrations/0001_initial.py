# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-19 10:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BasicArticle', '0002_articles_tags'),
        ('Community', '0005_community_image_thumbnail'),
        ('Media', '0002_media_medialink'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleFlagLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleScoreLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote', models.IntegerField(default=0, null=True)),
                ('downvote', models.IntegerField(default=0, null=True)),
                ('reported', models.IntegerField(default=0, null=True)),
                ('publish', models.BooleanField(default=False)),
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BasicArticle.Articles')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleUserScoreLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvoted', models.BooleanField(default=False)),
                ('downvoted', models.BooleanField(default=False)),
                ('reported', models.BooleanField(default=False)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicArticle.Articles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityReputaion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote_count', models.IntegerField(default=0)),
                ('downvote_count', models.IntegerField(default=0)),
                ('published_count', models.IntegerField(default=0)),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Community.Community')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FlagReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MediaFlagLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reputation.FlagReason')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Media.Media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MediaScoreLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote', models.IntegerField(default=0, null=True)),
                ('downvote', models.IntegerField(default=0, null=True)),
                ('reported', models.IntegerField(default=0, null=True)),
                ('publish', models.BooleanField(default=False)),
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Media.Media')),
            ],
        ),
        migrations.CreateModel(
            name='MediaUserScoreLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvoted', models.BooleanField(default=False)),
                ('downvoted', models.BooleanField(default=False)),
                ('reported', models.BooleanField(default=False)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Media.Media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_vote_unpublished', models.BooleanField(default=True)),
                ('upvote_value', models.IntegerField(default=0, null=True)),
                ('downvote_value', models.IntegerField(default=0, null=True)),
                ('can_report', models.BooleanField(default=True)),
                ('publish_value', models.IntegerField(default=0, null=True)),
                ('resource_type', models.CharField(default='resource', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.IntegerField(null=True)),
                ('publisher', models.IntegerField(null=True)),
                ('role_score', models.CharField(default='role_score', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='articleflaglogs',
            name='reason',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reputation.FlagReason'),
        ),
        migrations.AddField(
            model_name='articleflaglogs',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicArticle.Articles'),
        ),
        migrations.AddField(
            model_name='articleflaglogs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
