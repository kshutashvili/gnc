# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-25 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_auto_20171127_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435'),
        ),
    ]
