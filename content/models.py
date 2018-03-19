# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor.fields import RichTextField

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError


class MarketcapHistory(models.Model):
    timestamp = models.IntegerField(_("Timestamp"))
    date = models.DateField(_("Date"))
    month_number = models.IntegerField(_("Month number"))
    cap = models.DecimalField(_("Znaq index"),
                              max_digits=18,
                              decimal_places=7)

    class Meta:
        verbose_name = "История капитализации"
        verbose_name_plural = "История капитализации"

    def __unicode__(self):
        return str(self.date)


class Document(models.Model):
    title = models.CharField(_("Заголовок"),
                             max_length=255)
    content = RichTextField(_("Текст"))
    browser_title = models.CharField(_("Заголовок браузера"),
                                     max_length=128,
                                     default="ZNAQ|Document")
    slug = models.SlugField(_("Ссылка"),
                            max_length=128)
    created_dt = models.DateTimeField(_("Создано"),
                                      auto_now_add=True)
    updated_dt = models.DateTimeField(_("Оновлено"),
                                      auto_now=True)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __unicode__(self):
        return self.title


class ShortLink(models.Model):
    slug = models.SlugField(
        _("Отображаемая часть ссылки в адресной строке браузера"),
        help_text="wp, on, doc etc.",
        unique=True
    )
    link = models.CharField(
        _("Ссылка куда будет выполнено перенаправление"),
        max_length=128,
        unique=True
    )

    class Meta:
        verbose_name = "Сокращенная ссылка"
        verbose_name_plural = "Сокращенные ссылки"

    def __unicode__(self):
        return self.slug
