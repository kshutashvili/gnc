from django.template.defaulttags import register


@register.filter
def donation_wallet(profile_wallets_qs, currency):
    try:
        # get required field value
        return getattr(profile_wallets_qs.all()[0], currency.lower())
    except Exception as e:
        print e
        return "{} address will be added soon". format(currency.upper())
