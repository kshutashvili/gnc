"""indextrade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from two_factor.urls import urlpatterns as two_factor_urls

from django.conf.urls import url, include
from django.contrib import admin
from content.views import index
# from django.conf import settings
# from django.conf.urls.i18n import i18n_patterns
# from django.conf.urls.static import static
# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth import views as auth
# from django.core.urlresolvers import RegexURLPattern
#
# from content.views import (IndexView,
#                            IndexOldView,
#                            currency_list,
#                            BountyView,
#                            DocumentView,
#                            cap_history,
#                            bonuses_lk,
#                            redirect_to_link,
#                            PresskitView)
# from subscriptions.views import (subscribe, ask_question,
#                                  unsubscribe)
# from users.views import (ProfileView,
#                          set_user_settings,
#                          registration,
#                          log_in_user,
#                          # steps_check,
#                          step1_check,
#                          step2_check,
#                          ReferralProfile,
#                          save_wallet_for_bonus)
# from donations.views import save_transaction

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(two_factor_urls, 'two_factor')),
    url(r'$', index),
]

# decorators = [user_passes_test(lambda u: u.is_superuser)]
#
#
# def decorate_pattern(urlpattern):
#     callback = urlpattern.callback
#     for decorator in reversed(decorators):
#         callback = decorator(callback)
#
#     return RegexURLPattern(
#         urlpattern.regex.pattern,
#         callback,
#         urlpattern.default_args,
#         urlpattern.name
#     )
#
# two_factor_urls = [two_factor_urls[0]] + [decorate_pattern(pattern) for pattern in two_factor_urls[1:]]
#
# urlpatterns = i18n_patterns(
#     url(r'^admin/', admin.site.urls),
#     # url(r'', include('two_factor.urls', 'two_factor')),
#     url(r'', include(two_factor_urls, 'two_factor')),
#
#     # landing
#     url(r'^$', IndexView.as_view(), name='landing'),
#     url(r'^old/$', IndexOldView.as_view(), name='old'),
#     url(r'^subscription/$', subscribe, name='subscription'),
#     url(r'^unsubscribe/(?P<pk>[0-9]+)/$', unsubscribe, name='unsubscribe'),
#     url(r'^ask_question/$', ask_question, name='ask_question'),
#
#     # profile
#     url(r'^profile/$', ProfileView.as_view(), name='profile'),
#     url(r'^set_settings/$', set_user_settings, name='set_settings'),
#     url(r'^save_transaction', save_transaction, name='save_transaction'),
#     url(r'^set_wallet/$', save_wallet_for_bonus, name='set_wallet'),
#
#     # auth
#     url(r'^accounts/registration/$', registration, name="registration"),
#     url(r'^accounts/login/$', log_in_user, name="login"),
#     url(r'^accounts/logout/$', auth.logout, {'next_page': '/'}, name="logout"),
#     # url(r'^steps_check/$', steps_check, name="steps_check"),
#     url(r'^step1_check/$', step1_check, name="step1_check"),
#     url(r'^step2_check/$', step2_check, name="step2_check"),
#
#     url(r'^currencies/$', currency_list, name="currency_list"),
#
#     url(r'^bounty/$', BountyView.as_view(), name='bounty'),
#     url(r'^info/(?P<slug>[A-Za-z0-9-_]+)/$',
#         DocumentView.as_view(),
#         name='documents'),
#     url(r'^presskit/$',
#         PresskitView.as_view(),
#         name='presskit'),
#
#     # cap for landing calculator
#     url(r'^cap/', cap_history, name="cap_history"),
#
#     url(r'^bonuses/', bonuses_lk, name="bonuses_lk"),
#
#     url(r'^ref/', include('pinax.referrals.urls', namespace="pinax_referrals")),
#
#     url(r'^referral_profile/$', ReferralProfile.as_view(), name="referral_profile"),
#
#     url(r'^(?P<slug>[A-Za-z0-9-_]+)/$', redirect_to_link, name="short_link"),
#
# ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if 'rosetta' in settings.INSTALLED_APPS:
#     urlpatterns += i18n_patterns(
#         url(r'^rosetta/', include('rosetta.urls')),
#     )
