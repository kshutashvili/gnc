# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import DonationUserAddress, Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    def get_wallet_address(self, obj):
        return getattr(obj.ref_response.referral.user, obj.payment_method.lower())

    fields = ('payment_method',
              'donation_address',
              'e20_wallet',
              'tx_id',
              'tokens',
              'tx_sum',
              'user',
              'bonus_earned',
              'created_dt',
              'get_wallet_address'
              )
    readonly_fields = ["created_dt", "get_wallet_address"]

    get_wallet_address.short_description = "Адрес кошелька для отправки бонуса"


@admin.register(DonationUserAddress)
class DonationUserAddressAdmin(admin.ModelAdmin):
    pass
