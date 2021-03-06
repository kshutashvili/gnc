# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0033_auto_20171127_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationAddresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eth_address', models.CharField(max_length=50, verbose_name='\u0410\u0434\u0440\u0435\u0441 ETH')),
                ('btc_address', models.CharField(max_length=50, verbose_name='\u0410\u0434\u0440\u0435\u0441 BTC')),
                ('ltc_address', models.CharField(max_length=50, verbose_name='\u0410\u0434\u0440\u0435\u0441 LTC')),
                ('etc_address', models.CharField(max_length=50, verbose_name='\u0410\u0434\u0440\u0435\u0441 ETC')),
            ],
            options={
                'verbose_name': '\u0410\u0434\u0440\u0435\u0441\u0430 \u0434\u043b\u044f \u043f\u043e\u043a\u0443\u043f\u043a\u0438 \u0442\u043e\u043a\u0435\u043d\u043e\u0432',
            },
        ),
    ]
