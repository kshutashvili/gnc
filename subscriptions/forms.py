# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Subscription, ContactUs


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields['email'].error_messages['unique'] = _('Вы уже подписаны')
        self.fields['email'].widget.attrs = {
            'class': 'email',
            'placeholder': _(u'Введите Вашу электронную почту')
        }


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('email', 'message')

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['email'].error_messages['required'] = _('Все поля обязательны')
        self.fields['email'].widget.attrs = {
            'class': 'field',
            'placeholder': _(u'E-mail')
        }
        self.fields['message'].error_messages['required'] = _('Все поля обязательны')
        self.fields['message'].widget.attrs = {
            'class': 'field',
            'placeholder': _(u'Ваше сообщение')
        }
