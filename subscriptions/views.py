# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.utils.translation import ugettext_lazy as _
from django.http import (HttpResponseRedirect,
                         HttpResponse,
                         HttpResponseBadRequest)
from django.contrib.auth import get_user_model

from .models import Subscription
from .forms import SubscriptionForm, ContactUsForm
from .utils import UnsubscribeProcess


User = get_user_model()

class SubscriptionView(CreateView):
    model = Subscription
    form_class = SubscriptionForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        subscribe_form = SubscriptionForm(data=request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
        return redirect(self.success_url)


def subscribe(request):
    if request.method == 'POST':
        subscribe_form = SubscriptionForm(data=request.POST)
        response_data = {}
        if subscribe_form.is_valid():
            try:
                subscribe_form.save()
                # if not use str(), json.dump() raised is not JSON serializable error
                response_data['message'] = str(_('Вы успешно  подписались!'))
            except Exception as e:
                print e
                # if not use str(), json.dump() raised is not JSON serializable error
                response_data['message'] = str(_('Server error!'))
            return HttpResponse(json.dumps(response_data),
                                content_type="application/json")
        else:
            response_data['message'] = subscribe_form.errors["email"]
            return HttpResponse(json.dumps(response_data),
                                content_type="application/json")
    else:
        return HttpResponseBadRequest()


def ask_question(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(data=request.POST)
        response_data = {}
        if contact_form.is_valid():
            try:
                contact_form.save()
                # if not use str(), json.dump() raised is not JSON serializable error
                response_data['success'] = str(_('Мы с вами связемся в ближайшее время'))
            except Exception as e:
                print e
                # if not use str(), json.dump() raised is not JSON serializable error
                response_data['message'] = str(_('Server error!'))
            return HttpResponse(json.dumps(response_data),
                                content_type="application/json")
        else:
            # if not use str(), json.dump() raised is not JSON serializable error
            if "message" in contact_form.errors.keys():
                response_data['message'] = contact_form.errors["message"] # str(_('You are already subscribed'))
            if "email" in contact_form.errors.keys():
                response_data['message'] = contact_form.errors["email"]
            return HttpResponse(json.dumps(response_data),
                                content_type="application/json")
    else:
        return HttpResponseBadRequest()


def unsubscribe(request, pk):
    user_obj = get_object_or_404(User, pk=pk)

    UnsubscribeProcess(user_obj.email)

    return render(request, "email/unsubscribe.html", {})
