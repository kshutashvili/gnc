# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from pinax.referrals.models import Referral

from django.shortcuts import render, redirect, reverse
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext as _
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

from .forms import (UserChangeForm, PasswordChangeForm, RegistrationForm,
                    LoginForm)
from donations.forms import DonationForm
from donations.models import Donation
from users.models import AvailableCountries, ReferralBonusStep
from config.models import DonationAddress


User = get_user_model()


class ProfileView(TemplateView):
    template_name = "lk.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data()
        context['user_form'] = UserChangeForm(initial={
            'address': self.request.user.address,
            'phone_number': self.request.user.phone_number,
            'email': self.request.user.email})
        context['password_form'] = PasswordChangeForm(user=self.request.user)
        context['donation_form'] = DonationForm(self.request)
        context['donations'] = Donation.objects.filter(user=self.request.user).order_by('-created_dt')
        context['tokens_sum'] = Donation.objects.filter(user=self.request.user).aggregate(Sum('tokens'))['tokens__sum']
        context['addresses'] = DonationAddress.objects.all()

        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('landing')
        return super(ProfileView, self).dispatch(request, *args, **kwargs)


def set_user_settings(request):
    # previous_username = request.user.username
    if request.method == 'POST':
        response_data = {}
        user_form = UserChangeForm(instance=request.user,
                                   data=request.POST)
        password_form = PasswordChangeForm(request.user, request.POST)

        if user_form.is_valid():
            user_form.save()
            # if username not changed
            # if request.POST.get('username') == previous_username:
            #     response_data['username_changed'] = False
            #     pass
            # else:
            #     response_data['username_changed'] = True
            response_data['message'] = _("Сохранено")
        else:
            response_data['user_changed'] = False
            #print user_form.errors
            response_data['user_errors'] = user_form.errors

        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, request.user)
            response_data['password_changed'] = True
            response_data['message'] = _("Сохранено")
        else:
            #print password_form.errors
            response_data['password_changed'] = False
            if request.POST.get('old_password') or \
                request.POST.get('new_password1') or \
                request.POST.get('new_password2'):
                response_data['password_errors'] = password_form.errors
            else:
                response_data['password_errors'] = ''

        return HttpResponse(json.dumps(response_data),
                            content_type="application/json")

    return HttpResponseBadRequest()


def registration(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        response_data = {}
        if register_form.is_valid():
            register_form.save()
            cd = register_form.cleaned_data

            # before authentication and login!
            Referral.record_response(request, action_string="USER_SIGNUP")

            user = authenticate(username=cd['username'], password=cd['password1'])
            login(request, user)

            response_data['success'] = True
            response_data['message'] = _("Вы успешно зарегистрировались")
            # return HttpResponse(json.dumps(response_data), content_type="application/json")
            return HttpResponseRedirect("/")
        else:
            # print register_form.errors
            response_data['success'] = False
            response_data['message'] = register_form.errors
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponseBadRequest()


@csrf_exempt
def step2_check(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        response_data = {}
        if register_form.is_valid():
            response_data['success'] = True
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            if 'full_name' in register_form.errors or \
               'date_of_birth' in register_form.errors or \
               'country' in register_form.errors or \
               'state' in register_form.errors or \
               'city' in register_form.errors:
                response_data['success'] = False
            else:
                response_data['success'] = True
            response_data['message'] = register_form.errors
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponseBadRequest()


@csrf_exempt
def step1_check(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        response_data = {}
        if register_form.is_valid():
            response_data['success'] = True
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            if 'username' in register_form.errors or 'email' in register_form.errors or 'password1' in register_form.errors or 'password2' in register_form.errors:
                response_data['success'] = False
            else:
                response_data['success'] = True
            response_data['message'] = register_form.errors
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponseBadRequest()


def log_in_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request, request.POST)
        response_data = {}
        if login_form.is_valid():
            user = login_form.get_user()

            if user.is_superuser:
                response_data['message'] = _("Администратор должен входить через admin URL")
                return HttpResponse(json.dumps(response_data), content_type="application/json")

            remember_me = request.POST.get('remember', None)
            if not remember_me:
                request.session.set_expiry(0)

            login(request, user)

            response_data['success'] = True
            response_data['message'] = _("Вы вошли")
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            response_data['success'] = False
            response_data['message'] = _("Не правильный username или пароль")
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponseBadRequest()


class ReferralProfile(TemplateView):
    template_name = "referral_profile.html"

    def get_context_data(self, **kwargs):
        context = super(ReferralProfile, self).get_context_data()

        context['ref_steps'] = ReferralBonusStep.objects.all()
        steps_count = ReferralBonusStep.objects.count()
        print (55 / (steps_count - 1)) * steps_count
        context['steps_margin'] = 55 / (steps_count - 1)
        context['first_step_margin'] = steps_count
        context['progress_fill'] = (55 / (steps_count - 1)) + 5 + 9

        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('landing')
        return super(ReferralProfile, self).dispatch(request, *args, **kwargs)


def save_wallet_for_bonus(request):
    if request.method == 'POST':
        response_data = {}
        wallet_address = request.POST.get("wallet", None)
        currency = request.POST.get("currency", None)
        if wallet_address and currency:
            user = User.objects.get(id=request.user.id)
            setattr(user, currency.lower(), wallet_address)
            user.save()
            response_data = {'response': "ok"}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponseBadRequest()
