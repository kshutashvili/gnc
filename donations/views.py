# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from pinax.referrals.models import Referral

from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.http import (HttpResponse,
                         HttpResponseBadRequest)

from .forms import DonationForm
from .models import Donation


def save_transaction(request):
    if request.method == 'POST':
        form = DonationForm(request,
                            request.POST)
        response_data = {}

        if form.is_valid():
            if form.cleaned_data["payment_method"] != Donation.PAYMENT_METHOD.ETH \
               and not form.cleaned_data["tx_id"]:

                response_data['transaction_error'] = {}
                response_data['transaction_error']['tx_id'] = [str(_("Для не ETH транзакций это поле обязательно"))]

                return HttpResponse(json.dumps(response_data),
                                    content_type="application/json")
            else:
                donat_obj = form.save()

                # creating referral response
                ref_response_obj = Referral.record_response(
                    request,
                    action_string="PURCHASED"
                )

                # linking referral response with donation
                if ref_response_obj:
                    donat_obj.ref_response = ref_response_obj
                    donat_obj.save()

                response_data['message'] = str(_('Transaction saved!'))
                response_data['donation_obj'] = {
                    'date': donat_obj.created_dt.strftime("%d.%m.%y"),
                    'method': donat_obj.payment_method
                }
                return HttpResponse(json.dumps(response_data),
                                    content_type="application/json")
        else:
            response_data['transaction_error'] = form.errors
            return HttpResponse(json.dumps(response_data),
                                content_type="application/json")
    else:
        return HttpResponseBadRequest()
