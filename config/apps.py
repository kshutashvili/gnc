# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class ConfigConfig(AppConfig):
    name = 'config'

    def ready(self):
        import config.signals  # noqa
