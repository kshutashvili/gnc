# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import tinify

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import LandingPhoto


@receiver(post_save, sender=LandingPhoto)
def compress_image(sender, instance, **kwargs):
    # set API key
    tinify.key = settings.TINIFY_KEY
    # compress image
    try:
        # try compresing image
        tinify.from_file(instance.image.path).to_file(instance.image.path)
    except Exception:
        # return no compressed image
        return
