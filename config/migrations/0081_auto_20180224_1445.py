# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-24 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0080_auto_20180224_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingconfiguration3',
            name='donation_guide_doc_en',
            field=models.TextField(default='#', null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044e \u043f\u043e\u043a\u0443\u043f\u043a\u0438 \u0442\u043e\u043a\u0435\u043d\u043e\u0432 (\u041b\u041a)'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='donation_guide_doc_ru',
            field=models.TextField(default='#', null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044e \u043f\u043e\u043a\u0443\u043f\u043a\u0438 \u0442\u043e\u043a\u0435\u043d\u043e\u0432 (\u041b\u041a)'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='donation_guide_video_en',
            field=models.TextField(default='#', null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0412\u0438\u0434\u0435\u043e-\u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044e (\u041b\u041a)'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='donation_guide_video_ru',
            field=models.TextField(default='#', null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0412\u0438\u0434\u0435\u043e-\u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044e (\u041b\u041a)'),
        ),
    ]
