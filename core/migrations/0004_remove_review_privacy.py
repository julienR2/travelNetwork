# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-06 13:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170106_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='privacy',
        ),
    ]
