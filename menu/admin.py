# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": (
            ('name_en',
             'name_ru'),
            ('link',),
            ('order',)
        )
        }
        ),
    )
