# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 03:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 19, 3, 38, 34, 50738)),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 19, 3, 38, 34, 49864)),
        ),
    ]