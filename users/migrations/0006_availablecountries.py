# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20171214_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableCountries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', django_countries.fields.CountryField(max_length=746, multiple=True)),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u043c \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0430 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f',
            },
        ),
    ]
