# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class DonationsConfig(AppConfig):
    name = 'donations'

    def ready(self):
        import donations.signals  # noqa
