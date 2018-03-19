# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class MenuItem(models.Model):
    name = models.CharField(_('Название'),
                            max_length=50)
    link = models.CharField(_('Ссылка'),
                            max_length=255,
                            help_text='Примеры: #ico #subscribe #currency '\
                                      '#about #exchange #roadmap #emission '\
                                      '#takermaker #smartcontract #sales'\
                                      '#bonus #bounty #team #blog #faq #contact-us',
                            blank=True)
    order = models.IntegerField(_('Порядок'),
                                default=0)

    class Meta:
        verbose_name = _('Пункт меню')
        verbose_name_plural = _('Пункты меню')
        ordering = ['order', ]

    def __unicode__(self):
        return self.name
