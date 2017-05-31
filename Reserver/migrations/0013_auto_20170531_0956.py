# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 09:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserver', '0012_auto_20170530_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='openTime',
            field=models.DateField(default=datetime.date(2017, 5, 31)),
        ),
        migrations.AlterField(
            model_name='flat',
            name='openTimeEnd',
            field=models.DateField(default=datetime.date(2017, 5, 31)),
        ),
        migrations.AlterField(
            model_name='reserved',
            name='beginDate',
            field=models.DateField(default=datetime.date(2017, 5, 31)),
        ),
        migrations.AlterField(
            model_name='reserved',
            name='endDate',
            field=models.DateField(default=datetime.date(2017, 5, 31)),
        ),
    ]