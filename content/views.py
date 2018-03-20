# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import json
import datetime
import pytz

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, Http404
from django.utils import translation

from subscriptions.forms import SubscriptionForm, ContactUsForm
from config.models import (FooterMenuCategory,
                           AnswerQuestion,
                           Publication,
                           Exhibition,
                           Teammate,
                           Adviser,
                           RatedBy,
                           Partner,
                           LandingPhoto,
                           LandingConfiguration,
                           LandingConfiguration2)
from users.forms import LoginForm, RegistrationForm
from .models import Document, ShortLink


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        # date_now = datetime.datetime.now().replace(tzinfo=None)
        # date_end = LandingConfiguration.get_solo().discount_timer.replace(tzinfo=None)
        # timer = date_end - date_now
        # hours = (timer.total_seconds() / 86400 - timer.days) * 60
        # minutes = (hours - int(hours)) * 60
        # seconds = (minutes - int(minutes)) * 60
        # context['discount_timer'] = date_end - date_now
        # context['discount_timer_hours'] = int(hours)
        # context['discount_timer_minutes'] = int(minutes)
        # context['discount_timer_seconds'] = int(seconds)
        #context['subscribe_form'] = SubscriptionForm()
        #context['footer_menu'] = FooterMenuCategory.objects.all()

        #faq_count = AnswerQuestion.objects.count() // 2
        #context['faq_left'] = AnswerQuestion.objects.all()[faq_count:]
        #context['faq_right'] = AnswerQuestion.objects.all()[:faq_count]

        #context['publications'] = Publication.objects.all()
        #context['exhibitions'] = Exhibition.objects.all()

        #context['teammates'] = Teammate.objects.all()
        #context['advisers'] = Adviser.objects.all()

        #context['contact_us'] = ContactUsForm()

        #context['register_form'] = RegistrationForm()
        #context['login_form'] = LoginForm()

        #context['partners'] = Partner.objects.displayed()
        #context['ratedby_objects'] = RatedBy.objects.displayed()

        #context['landing_photos'] = LandingPhoto.objects.showed_photos()

        return context


class IndexOldView(TemplateView):
    template_name = "index_old.html"


class BountyView(TemplateView):
    template_name = "bounty.html"

    def get_context_data(self, **kwargs):
        context = super(BountyView, self).get_context_data()
        context['register_form'] = RegistrationForm()
        context['login_form'] = LoginForm()

        return context


class DocumentView(DetailView):
    model = Document
    template_name = "document.html"

    def get_context_data(self, **kwargs):
        context = super(DocumentView, self).get_context_data()
        context['register_form'] = RegistrationForm()
        context['login_form'] = LoginForm()

        return context


def currency_list(request):
    response = {}
    curr_list_response = requests.get('https://znaq.com/en/currencies/')
    response['currency'] = curr_list_response.json()
    response['eth_int'] = int(float(curr_list_response.json()["ZNAQ/ETH"][0]) * (10 ** 18))
    response['eth_str'] = str(int(float(curr_list_response.json()["ZNAQ/ETH"][0]) * (10 ** 18)))
    token_count_response = requests.get('http://znaq.com/en/token_count/')
    response['token_count'] = token_count_response.json()['tokens']
    return HttpResponse(json.dumps(response),
                                   content_type="application/json")


def cap_history(request):
    response = {}
    try:
        curr_list_response = requests.get('https://znaq.com/en/last_cap/')
        response['cap'] = curr_list_response.json()["last_cap"]
    except Exception as e:
        print e
        return HttpResponse(json.dumps({"cap": None}),
                                   content_type="application/json")
    return HttpResponse(json.dumps(response),
                                   content_type="application/json")


def bonuses_lk(request):
    response = {}
    config = LandingConfiguration2.get_solo()
    response["bonuses"] = [
        # "50"              "+5,5% -> 5.5"
        [
            config.bar5_price,
            float(config.bonus_to_float(config.bar5_bonus))
        ],
        [
            config.bar4_price,
            float(config.bonus_to_float(config.bar4_bonus))
        ],
        [
            config.bar3_price,
            float(config.bonus_to_float(config.bar3_bonus))
        ],
        [
            config.bar2_price,
            float(config.bonus_to_float(config.bar2_bonus))
        ],
        [
            config.bar1_price,
            float(config.bonus_to_float(config.bar1_bonus))
        ],
        [
            0,
            0
        ],
    ]
    return HttpResponse(json.dumps(response),
                        content_type="application/json")


def redirect_to_link(request, slug):
    short_link = get_object_or_404(ShortLink, slug=slug)

    return redirect(short_link.link)


class PresskitView(TemplateView):
    template_name = "press_kit_page.html"


def open_pdf(request, name, lang):
    file = None
    if name == 'onepager':
        if lang == 'ru':
            file = LandingConfiguration.get_solo().onepager_upload_ru
        elif lang == 'en':
            file = LandingConfiguration.get_solo().onepager_upload_en
    elif name == 'whitepaper':
        file = LandingConfiguration.get_solo().whitepaper_upload
    if file:
        file_data = open(file.path, 'rb').read()
        return HttpResponse(file_data, content_type='application/pdf')
    else:
        raise Http404

