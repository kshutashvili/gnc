# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from menu.models import MenuItem


def menu(request):
    return {"menu": MenuItem.objects.all()}
