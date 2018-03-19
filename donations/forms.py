# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from .models import Donation, DonationUserAddress
from .validators import eth_address_validator


class DonationForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields = ('payment_method', 'donation_address', 'e20_wallet',
                  'tx_id', 'user')

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(DonationForm, self).__init__(*args, **kwargs)

        self.fields['e20_wallet'].widget.attrs = {
            'class': 'input',
            'placeholder': _(u'Введите адрес вашего кошелька')
        }

        self.fields['tx_id'].error_messages['required'] = _(
            'Для не ETH транзакций это поле обязательно')
        self.fields['tx_id'].widget.attrs = {
            'class': 'input',
            'placeholder': _(u'Введите id транзакции')
        }

        self.fields['payment_method'].error_messages['required'] = _(
            'Выберите метод оплаты')

        self.fields['donation_address'].error_messages['required'] = _(
            'Выберите метод оплаты')

    def save(self, commit=True):

        ret = super(DonationForm, self).save(commit=commit)

        if commit:
            # save address
            DonationUserAddress.objects.get_or_create(
                user=self.request.user,
                e20_wallet=ret.e20_wallet
            )

        return ret

    def clean_user(self):
        return self.request.user

    def clean_e20_wallet(self):
        e20_wallet = self.cleaned_data['e20_wallet']
        eth_address_validator(e20_wallet)
        return e20_wallet
