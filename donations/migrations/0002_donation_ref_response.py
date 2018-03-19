# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-28 11:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0002_auto_20180130_0904'),
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='ref_response',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='referrals.ReferralResponse', verbose_name='Ref purchase'),
        ),
    ]
