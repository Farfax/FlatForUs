# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-10 22:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserver', '0013_auto_20170531_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='openTime',
            field=models.DateField(default=datetime.date(2017, 6, 10)),
        ),
        migrations.AlterField(
            model_name='flat',
            name='openTimeEnd',
            field=models.DateField(default=datetime.date(2017, 6, 10)),
        ),
        migrations.AlterField(
            model_name='reserved',
            name='beginDate',
            field=models.DateField(default=datetime.date(2017, 6, 10)),
        ),
        migrations.AlterField(
            model_name='reserved',
            name='endDate',
            field=models.DateField(default=datetime.date(2017, 6, 10)),
        ),
        migrations.AlterField(
            model_name='town',
            name='townName',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]