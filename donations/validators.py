# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from eth_utils.address import is_address


def eth_address_validator(value):
    if not is_address(value):
        raise ValidationError(
            _(u"Введите валидный ethereum адрес")
        )
