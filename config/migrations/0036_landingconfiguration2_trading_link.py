# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0035_auto_20171130_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingconfiguration2',
            name='trading_link',
            field=models.TextField(default='http://znaq.com/', verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 Trading-\u043f\u043b\u0430\u0442\u0444\u043e\u0440\u043c\u0443'),
        ),
    ]
