# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Reserver', '0008_auto_20170530_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flatName', models.CharField(max_length=60, unique=True)),
                ('canRent', models.BooleanField(default=False)),
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
                ('flatName', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Reserver.Flat')),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('townName', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='flat',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Reserver.Town'),
        ),
        migrations.AddField(
            model_name='flat',
            name='reservedDate',
            field=models.ManyToManyField(to='Reserver.Reserved'),
        ),
    ]
