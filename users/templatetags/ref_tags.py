from django.template.defaulttags import register

from donations.models import Donation


@register.filter
def action_filter(qs, action):
    return qs.filter(action=action)


@register.simple_tag
def purchased_amount_by_refs(responses):
    purchase_responses = responses.filter(action="PURCHASED")

    tokens_amount = 0
    purchase_amounts_list = []
    for purchase in purchase_responses:
        # list all transactions amounts for per user
        purchase_amounts_list.append(
            Donation.objects.filter(
                user=purchase.user,
                ref_response=purchase
            )[0].tokens or 0
        )
    tokens_amount += sum(purchase_amounts_list)
    return tokens_amount


@register.simple_tag
def calculate_bonus(donation_obj):
    try:
        if donation_obj.tx_sum:
            bonus = donation_obj.tx_sum / 100 * donation_obj.bonus_earned
        else:
            bonus = "Pending"
    except Exception as e:
        bonus = 0
    return bonus
