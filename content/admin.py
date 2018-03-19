# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Document, ShortLink


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    fields = (("title_en", "title_ru"),
              ("content_en", "content_ru"),
              ("browser_title_en", "browser_title_ru"),
              ("slug",))


@admin.register(ShortLink)
class ShortLinkAdmin(admin.ModelAdmin):
    pass
