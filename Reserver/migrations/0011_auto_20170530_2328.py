# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserver', '0010_remove_flat_reserveddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='canRent',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='reserved',
            name='isFree',
            field=models.BooleanField(default=True),
        ),
    ]
