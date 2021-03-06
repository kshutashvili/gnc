# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingconfiguration',
            name='discount_end_en',
            field=models.CharField(default='\u041a\u043e\u043d\u0435\u0446 \u0441\u043a\u0438\u0434\u043a\u0438:', max_length=32, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u043b\u0435 \u0441\u043a\u0438\u0434\u043a\u0438'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='discount_end_ru',
            field=models.CharField(default='\u041a\u043e\u043d\u0435\u0446 \u0441\u043a\u0438\u0434\u043a\u0438:', max_length=32, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u043b\u0435 \u0441\u043a\u0438\u0434\u043a\u0438'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='discount_info_en',
            field=models.CharField(default='\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0441\u043a\u0438\u0434\u043a\u0430:', max_length=32, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u0435\u0440\u0435\u0434 \u0441\u043a\u0438\u0434\u043a\u043e\u0439'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='discount_info_ru',
            field=models.CharField(default='\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0441\u043a\u0438\u0434\u043a\u0430:', max_length=32, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u0435\u0440\u0435\u0434 \u0441\u043a\u0438\u0434\u043a\u043e\u0439'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='onepager_link_en',
            field=models.TextField(null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 onepager'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='onepager_link_ru',
            field=models.TextField(null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 onepager'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='onepager_upload_en',
            field=models.FileField(null=True, upload_to='onepagers', verbose_name='\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c onepager'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='onepager_upload_ru',
            field=models.FileField(null=True, upload_to='onepagers', verbose_name='\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c onepager'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='raised_text_en',
            field=models.CharField(default='\u0421\u043e\u0431\u0440\u0430\u043d\u043e', max_length=32, null=True, verbose_name="\u0422\u0435\u043a\u0441\u0442 '\u0421\u043e\u0431\u0440\u0430\u043d\u043e'"),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='raised_text_ru',
            field=models.CharField(default='\u0421\u043e\u0431\u0440\u0430\u043d\u043e', max_length=32, null=True, verbose_name="\u0422\u0435\u043a\u0441\u0442 '\u0421\u043e\u0431\u0440\u0430\u043d\u043e'"),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='sale_btn_en',
            field=models.CharField(default='\u041d\u0410\u0428\u0418 \u0410\u041a\u0426\u0418\u0418', max_length=32, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u043e\u043f\u043a\u0438 \u043f\u043e\u0434 \u0442\u0430\u0439\u043c\u0435\u0440\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='sale_btn_ru',
            field=models.CharField(default='\u041d\u0410\u0428\u0418 \u0410\u041a\u0426\u0418\u0418', max_length=32, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u043e\u043f\u043a\u0438 \u043f\u043e\u0434 \u0442\u0430\u0439\u043c\u0435\u0440\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='timer_title_en',
            field=models.TextField(default='\u0414\u043e N-\u043d\u043e\u0439 \u043f\u0440\u043e\u0434\u0430\u0436\u0438 \u0442\u043e\u043a\u0435\u043d\u043e\u0432 \u043e\u0441\u0442\u0430\u043b\u043e\u0441\u044c:', null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0442\u0430\u0439\u043c\u0435\u0440\u0430'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='timer_title_ru',
            field=models.TextField(default='\u0414\u043e N-\u043d\u043e\u0439 \u043f\u0440\u043e\u0434\u0430\u0436\u0438 \u0442\u043e\u043a\u0435\u043d\u043e\u0432 \u043e\u0441\u0442\u0430\u043b\u043e\u0441\u044c:', null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0442\u0430\u0439\u043c\u0435\u0440\u0430'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='whitepaper_link_en',
            field=models.TextField(null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 whitepaper'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='whitepaper_link_ru',
            field=models.TextField(null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 whitepaper'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='whitepaper_upload_en',
            field=models.FileField(null=True, upload_to='whitepapers', verbose_name='\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c whitepaper'),
        ),
        migrations.AddField(
            model_name='landingconfiguration',
            name='whitepaper_upload_ru',
            field=models.FileField(null=True, upload_to='whitepapers', verbose_name='\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c whitepaper'),
        ),
    ]
