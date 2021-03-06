# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-18 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20180118_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='browser_title',
            field=models.CharField(default='ZNAQ|Document', max_length=128, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0430'),
        ),
        migrations.AddField(
            model_name='document',
            name='browser_title_en',
            field=models.CharField(default='ZNAQ|Document', max_length=128, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0430'),
        ),
        migrations.AddField(
            model_name='document',
            name='browser_title_ru',
            field=models.CharField(default='ZNAQ|Document', max_length=128, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0430'),
        ),
    ]
