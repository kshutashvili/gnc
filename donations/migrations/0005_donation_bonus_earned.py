# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-11 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0004_auto_20180311_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='bonus_earned',
            field=models.FloatField(blank=True, default=0, verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0431\u043e\u043d\u0443\u0441\u0430, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u0431\u0443\u0434\u0435\u0442 \u0440\u0430\u0441\u0447\u0438\u0442\u0430\u043d\u0430 \u044d\u0442\u0430 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f'),
        ),
    ]
