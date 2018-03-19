# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pinax.referrals.models import Referral

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.core.mail import EmailMultiAlternatives

from subscriptions.models import Subscription
from .models import (User, ReferralBonus, ReferralBonusStep,
                     ProfileWallet)
from config.models import EmailConfig


@receiver(post_save, sender=User)
def registration_notification(sender, instance, **kwargs):
    if kwargs['created']:
        email_config = EmailConfig.get_solo()
        html_body = render_to_string(
            "email/registration.html",
            {
                "message": email_config.register_text
            }
        )
        subject = email_config.register_subject
        mail = EmailMultiAlternatives(
            subject,
            '',
            "ZNAQ {}".format(email_config.default_from_email),
            [instance.email, ]
        )
        mail.attach_alternative(html_body, "text/html")
        mail.send()


@receiver(post_save, sender=User)
def subscribe_user(sender, instance, **kwargs):
    """
    this signal called twice:
    1. when User object created
    2. when User log in on the site (this call creating LogEntry instance
        and set changes to last_login field in User model)
    to prevent this used if statement
    """
    if kwargs['created']:
        user_subscription = Subscription(email=instance.email)
        user_subscription.save()


@receiver(post_save, sender=Referral)
def create_referral_bonus(sender, instance, **kwargs):
    try:
        initial_ref_percent = ReferralBonusStep.objects.get(step=0)
    except Exception:
        initial_ref_percent = 0
    # for each Referral must be created ReferralBonus obj
    ref_bonus = ReferralBonus.objects.create(
        user=instance.user,
        value=initial_ref_percent.value
    )


@receiver(post_save, sender=User)
def set_user_wallets(sender, instance, **kwargs):
    if kwargs['created']:
        wallets_obj = ProfileWallet.objects.filter(
            used_by_user=False
        ).first()
        if wallets_obj:
            wallets_obj.user = instance
            wallets_obj.used_by_user = True
            wallets_obj.save()
