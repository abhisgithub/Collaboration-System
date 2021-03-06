# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-24 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('desc', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('from_state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fromtransitions', to='workflow.States')),
                ('to_state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='totransitions', to='workflow.States')),
            ],
        ),
    ]
