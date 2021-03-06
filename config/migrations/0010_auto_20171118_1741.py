# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0009_auto_20171118_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_descr',
            field=models.TextField(blank=True, verbose_name="\u0422\u0435\u043a\u0441\u0442 \u0431\u043b\u043e\u043a\u0430 'exchange'"),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_descr_en',
            field=models.TextField(blank=True, null=True, verbose_name="\u0422\u0435\u043a\u0441\u0442 \u0431\u043b\u043e\u043a\u0430 'exchange'"),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_descr_ru',
            field=models.TextField(blank=True, null=True, verbose_name="\u0422\u0435\u043a\u0441\u0442 \u0431\u043b\u043e\u043a\u0430 'exchange'"),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_title',
            field=models.TextField(blank=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 'exchange'"),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_title_en',
            field=models.TextField(blank=True, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 'exchange'"),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_title_ru',
            field=models.TextField(blank=True, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 'exchange'"),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_triangle_text1',
            field=models.TextField(blank=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u043f\u0435\u0440\u0432\u044b\u043c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_triangle_text1_en',
            field=models.TextField(blank=True, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u043f\u0435\u0440\u0432\u044b\u043c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_triangle_text1_ru',
            field=models.TextField(blank=True, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u043f\u0435\u0440\u0432\u044b\u043c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_triangle_text2',
            field=models.TextField(blank=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u0432\u0442\u043e\u0440\u044b\u043c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_triangle_text2_en',
            field=models.TextField(blank=True, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u0432\u0442\u043e\u0440\u044b\u043c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_triangle_text2_ru',
            field=models.TextField(blank=True, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u0432\u0442\u043e\u0440\u044b\u043c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_triangle_text3',
            field=models.TextField(blank=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u0442\u0440\u0435\u0442\u044c\u0438\u043c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_triangle_text3_en',
            field=models.TextField(blank=True, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u0442\u0440\u0435\u0442\u044c\u0438\u043c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_triangle_text3_ru',
            field=models.TextField(blank=True, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u0442\u0440\u0435\u0442\u044c\u0438\u043c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_triangle_text4',
            field=models.TextField(blank=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u0447\u0435\u0442\u0432\u0451\u0440\u0442\u044b\u043c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_triangle_text4_en',
            field=models.TextField(blank=True, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u0447\u0435\u0442\u0432\u0451\u0440\u0442\u044b\u043c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='exchange_triangle_text4_ru',
            field=models.TextField(blank=True, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u0447\u0435\u0442\u0432\u0451\u0440\u0442\u044b\u043c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u043c'),
        ),
    ]
