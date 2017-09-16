# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BonaB', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cryptocurrency',
            name='fullNodes',
        ),
        migrations.AddField(
            model_name='fullnode',
            name='cryptoCurrency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BonaB.CryptoCurrency'),
        ),
    ]