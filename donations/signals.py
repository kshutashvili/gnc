# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F

from users.models import ReferralBonus, ReferralBonusStep
from .models import Donation


@receiver(post_save, sender=Donation)
def update_referral_bonus(sender, instance, **kwargs):
    if not kwargs['created'] and instance.ref_response:
        # new amount of tokens
        tokens = instance.tokens or 0

        # old amount of tokens
        previous_tokens = getattr(instance, '__original_tokens') or 0

        # getting referral bonus object of user
        # which asociated with current donation
        # through referral response
        ref_bonus_obj = ReferralBonus.objects.filter(
            pk=instance.ref_response.referral.user.referral_bonus.pk
        )

        # if object exist and value of tokens has changed
        if ref_bonus_obj and instance.tokens_has_changed():

            # updating value of token which bought by referral users
            ref_bonus_obj.update(
                purchase_amount=F('purchase_amount') - previous_tokens + tokens)

            # getting bonus value from BonusValueStep
            increased_bonus = ReferralBonusStep.objects.filter(
                step__lte=ref_bonus_obj[0].purchase_amount
            )

            # if exists, update referral bonus value with first
            # matched bonus
            if increased_bonus:
                if increased_bonus.last().step <= ref_bonus_obj[0].purchase_amount:
                    ref_bonus_obj.update(
                        value=increased_bonus.last().value
                    )
            else:
                # if not exists
                # that means purchase_amount is greater than
                # biggest BonusStep value. Updating with biggest step
                ref_bonus_obj.update(
                    value=ReferralBonusStep.objects.last().value
                )

            # getting bonus and amount of tokens bought by ref users
            purchase_amount = ref_bonus_obj[0].purchase_amount
            # if parner_value bonus is exist, use this
            bonus_value = ref_bonus_obj[0].partner_value or ref_bonus_obj[0].value

            # calculate bonus tokens
            bonus_tokens = (purchase_amount / 100) * bonus_value

            ref_bonus_obj.update(
                bonus_tokens=bonus_tokens
            )
