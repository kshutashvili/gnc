# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-08 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0084_presskit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presskit',
            name='download_btn_text',
            field=models.CharField(default='Download', max_length=32, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u043d\u043e\u043f\u043a\u0438 Download'),
        ),
        migrations.AlterField(
            model_name='presskit',
            name='download_btn_text_en',
            field=models.CharField(default='Download', max_length=32, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u043d\u043e\u043f\u043a\u0438 Download'),
        ),
        migrations.AlterField(
            model_name='presskit',
            name='download_btn_text_ru',
            field=models.CharField(default='Download', max_length=32, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u043d\u043e\u043f\u043a\u0438 Download'),
        ),
    ]
