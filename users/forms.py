# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import (UserCreationForm,
                                       AuthenticationForm,
                                       PasswordChangeForm as DjangoPasswordChangeForm,
                                       UserChangeForm as DjangoUserChangeForm,
                                       UsernameField)

from users.models import AvailableCountries


User = get_user_model()


class PasswordChangeForm(DjangoPasswordChangeForm):
    old_password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': False,
                                          'class': 'input password',
                                          'placeholder': _('Текущий пароль')}),
        required=False
    )
    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'input password',
                                          'placeholder': _('Новый пароль')}),
        required=False,
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'input password',
                                          'placeholder': _('Повторите новый пароль')}),
        required=False
    )


class UserChangeForm(DjangoUserChangeForm):
    class Meta:
        model = User
        fields = ('password', 'address', 'phone_number', 'email')
        field_classes = {'username': UsernameField}
        widgets = {'address': forms.TextInput(attrs={'class': 'input',
                                                     'placeholder': _('Ваш адрес')}),
                   'phone_number': forms.TextInput(attrs={'class': 'input',
                                                    'placeholder': _('Номер вашего телефона')}),
                   'email': forms.EmailInput(attrs={'class': 'input',
                                                       'placeholder': _('Ваш e-mail адрес')}),}


class RegistrationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _("Пароли не совпадают"),
        'terms_not_confirmed': _("Confirm terms required."),
        'country_not_valid': _("Резидентам выбранной вами страны регистрация не разрешена"),
        'full_name_required': _("Обязательное поле."),
        'date_of_birth_required': _("Дата должна быть заполнена полностью"),
        'country_required': _("Обязательное поле."),
        'city_required': _("Обязательное поле."),
        'state_required': _("Обязательное поле."),
    }

    password1 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'class': 'input-field',
                                                                  'placeholder': _('Пароль'),
                                                                  'required': 'True'}))
    password2 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'class': 'input-field',
                                                                  'placeholder': _('Подтверждение пароля'),
                                                                  'required': 'True'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'confirm_terms',
                  'date_of_birth', 'country', 'state', 'city')
        widgets = {'username': forms.TextInput(attrs={'class': 'input-field',
                                                      'placeholder': _('Username'),
                                                      'required': True}),
                   'email': forms.EmailInput(attrs={'class': 'input-field',
                                                    'placeholder': _('Email'),
                                                    'required': True}),
                   'full_name': forms.TextInput(attrs={'class': 'input-field',
                                                       'placeholder': _('Полное имя'),
                                                       'required': True}),
                   'date_of_birth': forms.DateInput(attrs={'class': 'input-field',
                                                       'placeholder': _('1990-05-31'),
                                                       'data-format': 'YYYY-MM-DD',
                                                       'data-template': 'YYYY MMMM D',
                                                       'required': True}),
                   'country': forms.Select(attrs={'class': 'input-field',
                                                  'placeholder': _('Страна'),
                                                  'required': True}),
                   'state': forms.TextInput(attrs={'class': 'input-field',
                                                   'placeholder': _('Штат/область'),
                                                   'required': True}),
                   'city': forms.TextInput(attrs={'class': 'input-field',
                                                  'placeholder': _('Город'),
                                                  'required': True}),
                   'confirm_terms': forms.CheckboxInput(attrs={'class': 'checkbox-field',
                                                               'id': 'agreement',
                                                               'required': True,
                                                               'disabled': 'True'}),}
        labels = {'username': '', 'email': '', 'full_name': '', 'country': ''}
        help_texts = {'username': ''}

  #  def clean_confirm_terms(self):
  #      confirm_terms = self.cleaned_data.get("confirm_terms")
  #      if not confirm_terms:
  #          raise forms.ValidationError(
  #              self.error_messages['terms_not_confirmed'],
  #              code='terms_not_confirmed',
  #          )
  #      return confirm_terms
#
  #  def clean_full_name(self):
  #      full_name = self.cleaned_data.get("full_name")
  #      if not full_name:
  #          raise forms.ValidationError(
  #              self.error_messages['full_name_required'],
  #              code='full_name_required',
  #          )
  #      return full_name
#
  #  def clean_date_of_birth(self):
  #      date_of_birth = self.cleaned_data.get("date_of_birth")
  #      if not date_of_birth:
  #          raise forms.ValidationError(
  #              self.error_messages['date_of_birth_required'],
  #              code='date_of_birth_required',
  #          )
  #      return date_of_birth
#
  #  def clean_city(self):
  #      city = self.cleaned_data.get("city")
  #      if not city:
  #          raise forms.ValidationError(
  #              self.error_messages['city_required'],
  #              code='city_required',
  #          )
  #      return city
#
  #  def clean_state(self):
  #      state = self.cleaned_data.get("state")
  #      if not state:
  #          raise forms.ValidationError(
  #              self.error_messages['state_required'],
  #              code='state_required',
  #          )
  #      return state
#
  #  def clean_country(self):
  #      country_list = [country.code for country in AvailableCountries.objects.get().countries]
  #      country = self.cleaned_data.get("country")
  #      if not country:
  #          raise forms.ValidationError(
  #              self.error_messages['country_required'],
  #              code='country_required',
  #          )
  #      if country not in country_list:
  #          raise forms.ValidationError(
  #              self.error_messages['country_not_valid'],
  #              code='country_not_valid',
  #          )
  #      return country


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'class': 'input login',
                   'placeholder': _('Username'),
                   'required': 'True'}
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'class': 'input password',
                   'placeholder': _('Пароль'),
                   'required': 'True'}
        )
    )
    remember = forms.BooleanField(
        label='',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'remember',
                                          'id': 'remember'}))
