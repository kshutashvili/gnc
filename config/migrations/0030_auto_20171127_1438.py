# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0029_auto_20171127_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingconfiguration2',
            name='team_title',
            field=models.TextField(blank=True, verbose_name='\u041d\u0430\u0448\u0430 \u043a\u043e\u043c\u0430\u043d\u0434\u0430'),
        ),
        migrations.AddField(
            model_name='landingconfiguration2',
            name='team_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='\u041d\u0430\u0448\u0430 \u043a\u043e\u043c\u0430\u043d\u0434\u0430'),
        ),
        migrations.AddField(
            model_name='landingconfiguration2',
            name='team_title_ru',
            field=models.TextField(blank=True, null=True, verbose_name='\u041d\u0430\u0448\u0430 \u043a\u043e\u043c\u0430\u043d\u0434\u0430'),
        ),
    ]
