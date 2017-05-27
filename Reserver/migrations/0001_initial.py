# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flatName', models.CharField(max_length=60)),
                ('isAvailable', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Reserved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginDate', models.DateField()),
                ('endDate', models.DateField()),
                ('isFree', models.BooleanField(default=False)),
                ('userName', models.CharField(default='Free', max_length=60)),
                ('flatName', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('townName', models.CharField(max_length=60)),
            ],
        ),
    ]
