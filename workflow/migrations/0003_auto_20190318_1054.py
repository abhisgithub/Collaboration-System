# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-18 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0005_community_image_thumbnail'),
        ('auth', '0008_alter_user_username_max_length'),
        ('workflow', '0002_auto_20190110_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='transitions',
            name='community',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community', to='Community.Community'),
        ),
        migrations.AddField(
            model_name='transitions',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role', to='auth.Group'),
        ),
    ]