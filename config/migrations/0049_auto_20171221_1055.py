# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-21 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0048_auto_20171221_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='footermenuitem',
            name='link_en',
            field=models.CharField(max_length=128, null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430'),
        ),
        migrations.AddField(
            model_name='footermenuitem',
            name='link_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430'),
        ),
    ]
