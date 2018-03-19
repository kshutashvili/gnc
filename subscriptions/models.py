# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .utils import SendSubscribeMail


class Subscription(models.Model):
    email = models.EmailField(_('Email подписчика'),
                              unique=True)
    subscribed_date = models.DateTimeField(_('Дата подписки'),
                                           auto_now_add=True)

    class Meta:
        verbose_name = _('Подписка на новости')
        verbose_name_plural = _('Подписки на новости')

    def save(self, *agrs, **kwargs):
        super(Subscription, self).save(*agrs, **kwargs)

        SendSubscribeMail(self.email)

    def __unicode__(self):
        return self.email


class ContactUs(models.Model):
    email = models.EmailField(_('Email подписчика'))
    message = models.TextField(_('Сообщение'))
    created = models.DateTimeField(_('Дата вопроса'),
                                   auto_now_add=True)

    class Meta:
        verbose_name = _('Вопрос')
        verbose_name_plural = _('Вопросы')

    def __unicode__(self):
        return self.email
