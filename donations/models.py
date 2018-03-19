# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pinax.referrals.models import ReferralResponse

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
# from .validators import eth_address_validator


class DonationUserAddress(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             blank=True,
                             verbose_name=_("Пользователь"),
                             related_name="addresses")

    e20_wallet = models.CharField(_("Адрес для получения токенов"),
                                  max_length=50)

    created_dt = models.DateTimeField(_("Дата создания"),
                                      auto_now_add=True)

    class Meta:
        verbose_name = _("Адрес пользователя")
        verbose_name_plural = _("Адреса пользователей")

    def __unicode__(self):
        return self.e20_wallet


class Donation(models.Model):

    class PAYMENT_METHOD:
        ETH = 'ETH'
        BTC = 'BTC'
        LTC = 'LTC'
        ETC = 'ETC'

        CHOICES = (
            (ETH, ETH),
            (BTC, BTC),
            (LTC, LTC),
            (ETC, ETC)
        )

        TX_ADDRESSES = {
            ETH: "https://etherscan.io/tx/{}",
            BTC: "https://blockchain.info/tx/{}",
            LTC: "https://live.blockcypher.com/ltc/tx/{}/",
            ETC: "https://gastracker.io/tx/{}"
        }

    payment_method = models.CharField(_("Тип оплаты"),
                                      max_length=5)

    donation_address = models.CharField(_("Адрес оплаты"),
                                        max_length=50)

    e20_wallet = models.CharField(_("Адрес для получения токенов"),
                                  max_length=50)

    tx_id = models.CharField(_("Номер транзакции"),
                             max_length=100,
                             blank=True,
                             null=True)

    tokens = models.FloatField(_("Количество токенов"),
                               blank=True,
                               null=True)
    tx_sum = models.FloatField(_("Сумма транзакции"),
                               blank=True,
                               null=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             blank=True,
                             verbose_name=_("Пользователь"),
                             related_name="donations")

    created_dt = models.DateTimeField(_("Дата создания"),
                                      auto_now_add=True)

    ref_response = models.OneToOneField(ReferralResponse,
                                        verbose_name=_("Ref purchase"),
                                        related_name="donation_response",
                                        blank=True,
                                        null=True)
    bonus_earned = models.FloatField(
        _("Значение бонуса, по которому будет расчитана эта транзакция"),
        blank=True,
        default=0
    )

    class Meta:
        verbose_name = _("Транзакция")
        verbose_name_plural = _("Транзакции")

    def __init__(self, *args, **kwargs):
        super(Donation, self).__init__(*args, **kwargs)

        # set previous tokens value
        setattr(self, '__original_%s' % 'tokens', getattr(self, 'tokens'))

    def save(self, force_insert=False, force_update=False):
        # updating bonus tokens, when bonus value changed in admin site
        if self.ref_response and not self.bonus_earned:
            if self.ref_response.referral.user.referral_bonus.partner_value:
                self.bonus_earned = self.ref_response.referral.user.referral_bonus.partner_value
            else:
                self.bonus_earned = self.ref_response.referral.user.referral_bonus.value

        super(Donation, self).save(force_insert, force_update)

    def tokens_has_changed(self):
        field = 'tokens'
        orig = '__original_%s' % field
        if getattr(self, orig) != getattr(self, field):
            return True
        return False

    def __unicode__(self):
        return "{0}-transaction to {1} with id {2}".format(
            self.payment_method,
            self.donation_address,
            self.tx_id or 'None')

    @property
    def tx_link(self):
        return self.PAYMENT_METHOD.TX_ADDRESSES[
            self.payment_method].format(self.tx_id)
