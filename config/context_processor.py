# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import FooterMenuCategory


def footer_menu(request):
    return {"footer_menu": FooterMenuCategory.objects.all()}
