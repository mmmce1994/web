# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BonaB', '0002_auto_20170914_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fullnode',
            name='port',
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='maxMoney',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='nSubsidyHalving',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='nTime',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='port',
            field=models.CharField(max_length=30),
        ),
    ]