# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-01 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0066_auto_20180201_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingconfiguration3',
            name='partners_block_title',
            field=models.TextField(default='Partners', verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 Partners'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='ratedby_block_title',
            field=models.TextField(default='Rated By', verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 Rated By'),
        ),
    ]
