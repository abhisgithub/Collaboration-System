# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-09-06 07:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0003_metadata_attrs'),
        ('BasicArticle', '0002_articles_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='metadata',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_metadata', to='metadata.Metadata'),
        ),
    ]