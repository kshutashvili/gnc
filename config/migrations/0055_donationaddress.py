# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-24 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0054_auto_20180124_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_name', models.CharField(default='Ethereum', help_text='Bitcoin, Ripple etc.', max_length=128, unique=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0412\u0430\u043b\u044e\u0442\u044b')),
                ('currency', models.CharField(default='ETH', help_text='BTC, ETH, LTC etc.', max_length=12, unique=True, verbose_name='\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043d\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u0430\u043b\u044e\u0442\u044b')),
                ('address', models.CharField(max_length=128, unique=True, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u043a\u043e\u0448\u0435\u043b\u044c\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u0410\u0434\u0440\u0435\u0441 \u0434\u043b\u044f \u043f\u043e\u043a\u0443\u043f\u043a\u0438 \u0442\u043e\u043a\u0435\u043d\u043e\u0432',
                'verbose_name_plural': '\u0410\u0434\u0440\u0435\u0441\u0430 \u0434\u043b\u044f \u043f\u043e\u043a\u0443\u043f\u043a\u0438 \u0442\u043e\u043a\u0435\u043d\u043e\u0432',
            },
        ),
    ]
