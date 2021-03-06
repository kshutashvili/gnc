# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-02 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0082_emailconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingconfiguration3',
            name='presentation_link',
            field=models.TextField(blank=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 Presentation'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='presentation_text',
            field=models.TextField(default='Presentation', verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u043e\u043f\u043a\u0438 Presentation'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='presentation_text_en',
            field=models.TextField(default='Presentation', null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u043e\u043f\u043a\u0438 Presentation'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='presentation_text_ru',
            field=models.TextField(default='Presentation', null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u043e\u043f\u043a\u0438 Presentation'),
        ),
    ]
