# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-23 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reputation', '0017_flagreasons_mediascorelog_mediauserscorelogs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FlagReasons',
            new_name='FlagReason',
        ),
    ]
