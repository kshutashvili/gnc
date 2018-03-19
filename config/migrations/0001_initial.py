# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandingConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timer_title', models.TextField(default='\u0414\u043e N-\u043d\u043e\u0439 \u043f\u0440\u043e\u0434\u0430\u0436\u0438 \u0442\u043e\u043a\u0435\u043d\u043e\u0432 \u043e\u0441\u0442\u0430\u043b\u043e\u0441\u044c:', verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0442\u0430\u0439\u043c\u0435\u0440\u0430')),
                ('timer_sale', models.DateField(verbose_name='\u0422\u0430\u0439\u043c\u0435\u0440')),
                ('raised_text', models.CharField(default='\u0421\u043e\u0431\u0440\u0430\u043d\u043e', max_length=32, verbose_name="\u0422\u0435\u043a\u0441\u0442 '\u0421\u043e\u0431\u0440\u0430\u043d\u043e'")),
                ('raised_value', models.CharField(help_text='$10 929 925', max_length=32, verbose_name="\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 '\u0421\u043e\u0431\u0440\u0430\u043d\u043e'")),
                ('sale_btn', models.CharField(default='\u041d\u0410\u0428\u0418 \u0410\u041a\u0426\u0418\u0418', max_length=32, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u043e\u043f\u043a\u0438 \u043f\u043e\u0434 \u0442\u0430\u0439\u043c\u0435\u0440\u043e\u043c')),
                ('discount_info', models.CharField(default='\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0441\u043a\u0438\u0434\u043a\u0430:', max_length=32, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u0435\u0440\u0435\u0434 \u0441\u043a\u0438\u0434\u043a\u043e\u0439')),
                ('discount', models.CharField(default='40%', max_length=10, verbose_name='\u0420\u0430\u0437\u043c\u0435\u0440 \u0441\u043a\u0438\u0434\u043a\u0438')),
                ('discount_end', models.CharField(default='\u041a\u043e\u043d\u0435\u0446 \u0441\u043a\u0438\u0434\u043a\u0438:', max_length=32, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u043b\u0435 \u0441\u043a\u0438\u0434\u043a\u0438')),
                ('discount_timer', models.DateField(verbose_name='\u0422\u0430\u0439\u043c\u0435\u0440 \u0441\u043a\u0438\u0434\u043a\u0438')),
                ('whitepaper_btn_text', models.TextField(default='White paper', verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u043e\u043f\u043a\u0438 whitepaper')),
                ('whitepaper_link', models.TextField(verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 whitepaper')),
                ('whitepaper_upload', models.FileField(upload_to='whitepapers', verbose_name='\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c whitepaper')),
                ('onepager_btn_text', models.TextField(default='One pager', verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u043e\u043f\u043a\u0438 onepager')),
                ('onepager_link', models.TextField(verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 onepager')),
                ('onepager_upload', models.FileField(upload_to='onepagers', verbose_name='\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c onepager')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f \u043b\u044d\u043d\u0434\u0438\u043d\u0433\u0430',
            },
        ),
    ]
