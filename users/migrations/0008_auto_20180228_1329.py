# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-28 11:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_referralbonus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='referralbonus',
            options={'verbose_name': 'Referral Bonus', 'verbose_name_plural': 'Referral Bonuses'},
        ),
    ]
