# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-24 13:24
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0053_auto_20180117_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingconfiguration3',
            name='blogging_bounty_text',
            field=ckeditor.fields.RichTextField(default='To take part in the Bloging & Vloging bounty campaign ...', verbose_name='Bloging & Vloging bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='blogging_bounty_text_en',
            field=ckeditor.fields.RichTextField(default='To take part in the Bloging & Vloging bounty campaign ...', null=True, verbose_name='Bloging & Vloging bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='blogging_bounty_text_ru',
            field=ckeditor.fields.RichTextField(default='To take part in the Bloging & Vloging bounty campaign ...', null=True, verbose_name='Bloging & Vloging bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='blogging_bounty_title',
            field=models.TextField(default='Bloging & Vloging bounty', verbose_name='Bloging & Vloging bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='blogging_bounty_title_en',
            field=models.TextField(default='Bloging & Vloging bounty', null=True, verbose_name='Bloging & Vloging bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='blogging_bounty_title_ru',
            field=models.TextField(default='Bloging & Vloging bounty', null=True, verbose_name='Bloging & Vloging bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='btalk_bounty_text',
            field=ckeditor.fields.RichTextField(default='To take part in the Bitcoin Talk bounty campaign ...', verbose_name='Bitcoin Talk bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='btalk_bounty_text_en',
            field=ckeditor.fields.RichTextField(default='To take part in the Bitcoin Talk bounty campaign ...', null=True, verbose_name='Bitcoin Talk bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='btalk_bounty_text_ru',
            field=ckeditor.fields.RichTextField(default='To take part in the Bitcoin Talk bounty campaign ...', null=True, verbose_name='Bitcoin Talk bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='btalk_bounty_title',
            field=models.TextField(default='Bitcoin Talk bounty', verbose_name='Bitcoin Talk bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='btalk_bounty_title_en',
            field=models.TextField(default='Bitcoin Talk bounty', null=True, verbose_name='Bitcoin Talk bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='btalk_bounty_title_ru',
            field=models.TextField(default='Bitcoin Talk bounty', null=True, verbose_name='Bitcoin Talk bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='community_bounty_text',
            field=ckeditor.fields.RichTextField(default='To take part in the Community bounty campaign ...', verbose_name='Community bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='community_bounty_text_en',
            field=ckeditor.fields.RichTextField(default='To take part in the Community bounty campaign ...', null=True, verbose_name='Community bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='community_bounty_text_ru',
            field=ckeditor.fields.RichTextField(default='To take part in the Community bounty campaign ...', null=True, verbose_name='Community bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='community_bounty_title',
            field=models.TextField(default='Community bounty', verbose_name='Community bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='community_bounty_title_en',
            field=models.TextField(default='Community bounty', null=True, verbose_name='Community bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='community_bounty_title_ru',
            field=models.TextField(default='Community bounty', null=True, verbose_name='Community bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='facebook_bounty_text',
            field=ckeditor.fields.RichTextField(default='To take part in the Facebook bounty campaign ...', verbose_name='Facebook bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='facebook_bounty_text_en',
            field=ckeditor.fields.RichTextField(default='To take part in the Facebook bounty campaign ...', null=True, verbose_name='Facebook bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='facebook_bounty_text_ru',
            field=ckeditor.fields.RichTextField(default='To take part in the Facebook bounty campaign ...', null=True, verbose_name='Facebook bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='facebook_bounty_title',
            field=models.TextField(default='Facebook bounty', verbose_name='Facebook bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='facebook_bounty_title_en',
            field=models.TextField(default='Facebook bounty', null=True, verbose_name='Facebook bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='facebook_bounty_title_ru',
            field=models.TextField(default='Facebook bounty', null=True, verbose_name='Facebook bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='instagram_bounty_text',
            field=ckeditor.fields.RichTextField(default='To take part in the Instagram bounty campaign ...', verbose_name='Instagram bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='instagram_bounty_text_en',
            field=ckeditor.fields.RichTextField(default='To take part in the Instagram bounty campaign ...', null=True, verbose_name='Instagram bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='instagram_bounty_text_ru',
            field=ckeditor.fields.RichTextField(default='To take part in the Instagram bounty campaign ...', null=True, verbose_name='Instagram bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='instagram_bounty_title',
            field=models.TextField(default='Instagram bounty', verbose_name='Instagram bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='instagram_bounty_title_en',
            field=models.TextField(default='Instagram bounty', null=True, verbose_name='Instagram bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='instagram_bounty_title_ru',
            field=models.TextField(default='Instagram bounty', null=True, verbose_name='Instagram bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='media_bounty_text',
            field=ckeditor.fields.RichTextField(default='To take part in the Media bounty campaign ...', verbose_name='Media bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='media_bounty_text_en',
            field=ckeditor.fields.RichTextField(default='To take part in the Media bounty campaign ...', null=True, verbose_name='Media bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='media_bounty_text_ru',
            field=ckeditor.fields.RichTextField(default='To take part in the Media bounty campaign ...', null=True, verbose_name='Media bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='media_bounty_title',
            field=models.TextField(default='Media bounty', verbose_name='Media bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='media_bounty_title_en',
            field=models.TextField(default='Media bounty', null=True, verbose_name='Media bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='media_bounty_title_ru',
            field=models.TextField(default='Media bounty', null=True, verbose_name='Media bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='medium_bounty_text',
            field=ckeditor.fields.RichTextField(default='To take part in the Medium bounty campaign ...', verbose_name='Medium bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='medium_bounty_text_en',
            field=ckeditor.fields.RichTextField(default='To take part in the Medium bounty campaign ...', null=True, verbose_name='Medium bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='medium_bounty_text_ru',
            field=ckeditor.fields.RichTextField(default='To take part in the Medium bounty campaign ...', null=True, verbose_name='Medium bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='medium_bounty_title',
            field=models.TextField(default='Medium bounty', verbose_name='Medium bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='medium_bounty_title_en',
            field=models.TextField(default='Medium bounty', null=True, verbose_name='Medium bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='medium_bounty_title_ru',
            field=models.TextField(default='Medium bounty', null=True, verbose_name='Medium bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='reddit_bounty_text',
            field=ckeditor.fields.RichTextField(default='To take part in the Reddit bounty campaign ...', verbose_name='Reddit bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='reddit_bounty_text_en',
            field=ckeditor.fields.RichTextField(default='To take part in the Reddit bounty campaign ...', null=True, verbose_name='Reddit bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='reddit_bounty_text_ru',
            field=ckeditor.fields.RichTextField(default='To take part in the Reddit bounty campaign ...', null=True, verbose_name='Reddit bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='reddit_bounty_title',
            field=models.TextField(default='Reddit bounty', verbose_name='Reddit bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='reddit_bounty_title_en',
            field=models.TextField(default='Reddit bounty', null=True, verbose_name='Reddit bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='reddit_bounty_title_ru',
            field=models.TextField(default='Reddit bounty', null=True, verbose_name='Reddit bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='referral_bounty_text',
            field=ckeditor.fields.RichTextField(default='To take part in the Referral bounty campaign ...', verbose_name='Referral bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='referral_bounty_text_en',
            field=ckeditor.fields.RichTextField(default='To take part in the Referral bounty campaign ...', null=True, verbose_name='Referral bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='referral_bounty_text_ru',
            field=ckeditor.fields.RichTextField(default='To take part in the Referral bounty campaign ...', null=True, verbose_name='Referral bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='referral_bounty_title',
            field=models.TextField(default='Referral bounty', verbose_name='Referral bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='referral_bounty_title_en',
            field=models.TextField(default='Referral bounty', null=True, verbose_name='Referral bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='referral_bounty_title_ru',
            field=models.TextField(default='Referral bounty', null=True, verbose_name='Referral bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='telegram_bounty_text',
            field=ckeditor.fields.RichTextField(default='To take part in the Telegram bounty campaign ...', verbose_name='Telegram bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='telegram_bounty_text_en',
            field=ckeditor.fields.RichTextField(default='To take part in the Telegram bounty campaign ...', null=True, verbose_name='Telegram bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='telegram_bounty_text_ru',
            field=ckeditor.fields.RichTextField(default='To take part in the Telegram bounty campaign ...', null=True, verbose_name='Telegram bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='telegram_bounty_title',
            field=models.TextField(default='Telegram bounty', verbose_name='Telegram bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='telegram_bounty_title_en',
            field=models.TextField(default='Telegram bounty', null=True, verbose_name='Telegram bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='telegram_bounty_title_ru',
            field=models.TextField(default='Telegram bounty', null=True, verbose_name='Telegram bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='tokenmarket_bounty_text',
            field=ckeditor.fields.RichTextField(default='To take part in the Token Market bounty campaign ...', verbose_name='Token Market bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='tokenmarket_bounty_text_en',
            field=ckeditor.fields.RichTextField(default='To take part in the Token Market bounty campaign ...', null=True, verbose_name='Token Market bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='tokenmarket_bounty_text_ru',
            field=ckeditor.fields.RichTextField(default='To take part in the Token Market bounty campaign ...', null=True, verbose_name='Token Market bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='tokenmarket_bounty_title',
            field=models.TextField(default='Token Market bounty', verbose_name='Token Market bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='tokenmarket_bounty_title_en',
            field=models.TextField(default='Token Market bounty', null=True, verbose_name='Token Market bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='tokenmarket_bounty_title_ru',
            field=models.TextField(default='Token Market bounty', null=True, verbose_name='Token Market bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='twitter_bounty_text',
            field=ckeditor.fields.RichTextField(default='To take part in the Twitter bounty campaign ...', verbose_name='Twitter bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='twitter_bounty_text_en',
            field=ckeditor.fields.RichTextField(default='To take part in the Twitter bounty campaign ...', null=True, verbose_name='Twitter bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='twitter_bounty_text_ru',
            field=ckeditor.fields.RichTextField(default='To take part in the Twitter bounty campaign ...', null=True, verbose_name='Twitter bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='twitter_bounty_title',
            field=models.TextField(default='Twitter bounty', verbose_name='Twitter bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='twitter_bounty_title_en',
            field=models.TextField(default='Twitter bounty', null=True, verbose_name='Twitter bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='twitter_bounty_title_ru',
            field=models.TextField(default='Twitter bounty', null=True, verbose_name='Twitter bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='youtube_bounty_text',
            field=ckeditor.fields.RichTextField(default='To take part in the Youtube bounty campaign ...', verbose_name='Youtube bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='youtube_bounty_text_en',
            field=ckeditor.fields.RichTextField(default='To take part in the Youtube bounty campaign ...', null=True, verbose_name='Youtube bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='youtube_bounty_text_ru',
            field=ckeditor.fields.RichTextField(default='To take part in the Youtube bounty campaign ...', null=True, verbose_name='Youtube bounty modal text'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='youtube_bounty_title',
            field=models.TextField(default='Youtube bounty', verbose_name='Youtube bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='youtube_bounty_title_en',
            field=models.TextField(default='Youtube bounty', null=True, verbose_name='Youtube bounty modal title'),
        ),
        migrations.AddField(
            model_name='landingconfiguration3',
            name='youtube_bounty_title_ru',
            field=models.TextField(default='Youtube bounty', null=True, verbose_name='Youtube bounty modal title'),
        ),
    ]
