# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-12 06:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20160912_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertlog',
            name='insert_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 12, 6, 3, 15, 48188)),
        ),
    ]
