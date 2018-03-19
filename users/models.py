# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_countries.fields import CountryField
from solo.models import SingletonModel

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _, ugettext

from subscriptions.models import Subscription


class User(AbstractUser):
    confirm_terms = models.BooleanField("Confirm terms",
                                        default=False)
    full_name = models.CharField(_('Full name'),
                                 max_length=60,
                                 blank=True)
    address = models.CharField(_('Address'),
                               max_length=128,
                               blank=True)
    phone_number = models.CharField(_("Phone number"),
                                    max_length=20,
                                    blank=True)
    email = models.EmailField(_('email address'),
                              unique=True)
    date_of_birth = models.DateField(_("Дата рождения"),
                                     blank=True,
                                     null=True)
    country = CountryField(_("Страна"),
                           blank=True,
                           blank_label=_("Страна"))
    state = models.CharField(_("Штат/Область"),
                             max_length=128,
                             blank=True)
    city = models.CharField(_("Город"),
                            max_length=128,
                            blank=True)

    # wallets for bonuses
    btc = models.CharField(
        _("Кошелек BTC"),
        max_length=48,
        blank=True
    )
    eth = models.CharField(
        _("Кошелек ETH"),
        max_length=48,
        blank=True
    )
    xrp = models.CharField(
        _("Кошелек XRP"),
        max_length=48,
        blank=True
    )
    bch = models.CharField(
        _("Кошелек BCH"),
        max_length=48,
        blank=True
    )
    ada = models.CharField(
        _("Кошелек ADA"),
        max_length=64,
        blank=True
    )
    xlm = models.CharField(
        _("Кошелек XLM"),
        max_length=64,
        blank=True
    )
    neo = models.CharField(
        _("Кошелек NEO"),
        max_length=48,
        blank=True
    )
    ltc = models.CharField(
        _("Кошелек LTC"),
        max_length=48,
        blank=True
    )
    eos = models.CharField(
        _("Кошелек EOS"),
        max_length=64,
        blank=True
    )
    xem = models.CharField(
        _("Кошелек XEM"),
        max_length=64,
        blank=True
    )
    dash = models.CharField(
        _("Кошелек DASH"),
        max_length=48,
        blank=True
    )
    etc = models.CharField(
        _("Кошелек ETC"),
        max_length=48,
        blank=True
    )


class AvailableCountries(SingletonModel):
    countries = CountryField(multiple=True)

    class Meta:
        verbose_name = _("Страны, которым разрешена регистрация")

    def __unicode__(self):
        return ugettext("Страны, которым разрешена регистрация")


class ReferralBonus(models.Model):
    user = models.OneToOneField(
        User,
        related_name="referral_bonus",
        verbose_name="Пользователь"
    )
    responses = models.IntegerField(
        _("Количество переходов по реф. ссылке"),
        default=0
    )
    signups = models.IntegerField(
        _("Количество регистраций по реф. ссылке"),
        default=0
    )
    purchases = models.IntegerField(
        _("Количество покупок по реф. ссылке"),
        default=0
    )
    purchase_amount = models.FloatField(
        _("Суммарное количество купленных токенов"),
        default=0
    )
    value = models.FloatField(
        _("Величина бонуса (в %)"),
        default=0
    )
    bonus_tokens = models.FloatField(
        _("Количество бонусных токенов"),
        default=0
    )
    partner_value = models.FloatField(
        _("Величина бонуса для Партнера (в %)"),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Referral Bonus"
        verbose_name_plural = "Referral Bonuses"

    def save(self, **kwargs):
        # updating bonus tokens, when bonus value changed in admin site
        if self.partner_value:
            self.bonus_tokens = (self.purchase_amount / 100) * self.partner_value
        else:
            self.bonus_tokens = (self.purchase_amount / 100) * self.value

        super(ReferralBonus, self).save(**kwargs)

    def __unicode__(self):
        return self.user.username


class ReferralBonusStep(models.Model):
    step = models.FloatField(
        _("Порог скидки (с какого количества токенов будет использоватся эта скидка)"),
        default=0,
        unique=True
    )
    value = models.FloatField(
        _("Скидка (в %)"),
        default=0,
        unique=True
    )

    class Meta:
        verbose_name = "Referral Bonus Step"
        verbose_name_plural = "Referral Bonus Steps"
        ordering = ('step',)

    def __unicode__(self):
        return "{0} tokens => {1} (%) referral bonus".format(
            self.step,
            self.value
        )


class ProfileWallet(models.Model):
    btc = models.CharField(
        _("Кошелек BTC"),
        max_length=128
    )
    eth = models.CharField(
        _("Кошелек ETH"),
        max_length=128
    )
    xrp = models.CharField(
        _("Кошелек XRP"),
        max_length=128
    )
    bch = models.CharField(
        _("Кошелек BCH"),
        max_length=128
    )
    ada = models.CharField(
        _("Кошелек ADA"),
        max_length=128
    )
    xlm = models.CharField(
        _("Кошелек XLM"),
        max_length=128
    )
    neo = models.CharField(
        _("Кошелек NEO"),
        max_length=128
    )
    ltc = models.CharField(
        _("Кошелек LTC"),
        max_length=128
    )
    eos = models.CharField(
        _("Кошелек EOS"),
        max_length=128
    )
    xem = models.CharField(
        _("Кошелек XEM"),
        max_length=128
    )
    dash = models.CharField(
        _("Кошелек DASH"),
        max_length=128
    )
    etc = models.CharField(
        _("Кошелек ETC"),
        max_length=128
    )

    user = models.ForeignKey(
        User,
        related_name='profile_wallets',
        verbose_name='Пользователь',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    used_by_user = models.BooleanField(
        _("Привязано к пользователю"),
        default=False
    )

    class Meta:
        verbose_name = "Profile Wallets"
        verbose_name_plural = "Profile Wallets"

    def __unicode__(self):
        if self.user:
            return "Used by {}".format(self.user.username)
        return "Free wallets"
