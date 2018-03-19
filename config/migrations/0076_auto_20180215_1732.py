# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-15 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0075_landingphoto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='landingphoto',
            options={'verbose_name': 'Photo', 'verbose_name_plural': 'Photo'},
        ),
        migrations.AddField(
            model_name='landingphoto',
            name='show',
            field=models.BooleanField(default=True, verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c?'),
        ),
        migrations.AlterField(
            model_name='landingphoto',
            name='image',
            field=models.ImageField(upload_to='compressed', verbose_name='Photo'),
        ),
    ]
