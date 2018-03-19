# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0045_auto_20171215_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingConfiguration3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onepager_upload', models.FileField(blank=True, upload_to='rulebook', verbose_name='\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c rulebook')),
                ('onepager_upload_en', models.FileField(blank=True, null=True, upload_to='rulebook', verbose_name='\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c rulebook')),
                ('onepager_upload_ru', models.FileField(blank=True, null=True, upload_to='rulebook', verbose_name='\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c rulebook')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f \u043b\u044d\u043d\u0434\u0438\u043d\u0433\u0430 \u0447.3',
            },
        ),
    ]
