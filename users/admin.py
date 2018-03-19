# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from solo.admin import SingletonModelAdmin

from django.contrib import admin
from django.conf.urls import url
from django.http import HttpResponseRedirect

from .models import (User, AvailableCountries,
                     ReferralBonus,
                     ReferralBonusStep,
                     ProfileWallet)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(AvailableCountries)
class AvailableCountriesAdmin(SingletonModelAdmin):
    pass


@admin.register(ReferralBonus)
class ReferralBonusAdmin(admin.ModelAdmin):
    exclude = ('responses', 'signups', 'purchases')


@admin.register(ReferralBonusStep)
class ReferralBonusStepAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfileWallet)
class ProfileWalletAdmin(admin.ModelAdmin):
    list_display = ['btc', 'user', 'used_by_user']
    list_filter = ('used_by_user',)
    exclude = ('user', 'used_by_user')
    change_list_template = "admin/profile_wallets_changelist.html"

    def get_urls(self):
        urls = super(ProfileWalletAdmin, self).get_urls()
        my_urls = [
            url(r'^set_wallets/$', self.set_wallets),
        ]
        return my_urls + urls

    def process_wallets(self, objects):
        wallets_obj = objects[0]  # get wallets
        user_obj = objects[1]  # get user
        try:
            # set wallet for user
            wallets_obj.user = user_obj
            wallets_obj.used_by_user = True
            wallets_obj.save()
        except Exception as e:
            print e

    def set_wallets(self, request):
        """
            custom action "Set wallets" button on list page
        """

        free_wallets = self.model.objects.filter(
            used_by_user=False
        )

        users_without_wallets = User.objects.filter(
            profile_wallets__isnull=True
        )

        # pass tuples (wallets, user) to process_wallets function
        map(self.process_wallets, zip(free_wallets, users_without_wallets))

        return HttpResponseRedirect("../")
