# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-17 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0052_auto_20180111_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landingconfiguration',
            name='slack',
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='bitcointalk',
            field=models.CharField(blank=True, max_length=64, verbose_name='Bitcointalk'),
        ),
    ]
