# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-13 03:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_auto_20160913_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertlog',
            name='insert_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
