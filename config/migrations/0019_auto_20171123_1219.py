# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0018_auto_20171123_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingconfiguration',
            name='exhibition_block_title_en',
            field=models.TextField(default='Exhibitions', null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 'Exhibition'"),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exhibition_block_title_ru',
            field=models.TextField(default='Exhibitions', null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 'Exhibition'"),
        ),
    ]
