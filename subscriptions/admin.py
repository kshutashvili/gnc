# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Subscription, ContactUs


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_date']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'created']
