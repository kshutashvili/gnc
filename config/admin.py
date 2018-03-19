# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from solo.admin import SingletonModelAdmin

from django.contrib import admin

from .models import (LandingConfiguration,
                     Teammate,
                     Adviser,
                     Publication,
                     Exhibition,
                     AnswerQuestion,
                     LandingConfiguration2,
                     LandingConfiguration3,
                     FooterMenuCategory,
                     FooterMenuItem,
                     DonationAddresses,
                     DonationAddress,
                     SaleStages,
                     CrowdsaleCurrencyIndex,
                     CrowdsaleInfo,
                     RatedBy,
                     Partner,
                     LandingPhoto,
                     EmailConfig,
                     PressKit,
                     ReferralSettings)


@admin.register(LandingConfiguration)
class LandingConfigurationAdmin(SingletonModelAdmin):
    fieldsets = (("Блок ICO", {"classes": ("collapse",),
                               "fields": (("timer_title_en",
                                           "timer_title_ru"),
                                          ("timer_sale",),
                                          ("sale_btn_en",
                                           "sale_btn_ru"),
                                          ("discount_info_en",
                                           "discount_info_ru"),
                                          ("discount_end_en",
                                           "discount_end_ru"),
                                          ("discount_timer",
                                           "discount"),
                                          ("whitepaper_btn_text"),
                                          ("whitepaper_link_en",
                                           "whitepaper_link_ru"),
                                          ("whitepaper_upload_en",
                                           "whitepaper_upload_ru"),
                                          ("onepager_btn_text"),
                                          ("onepager_link_en",
                                           "onepager_link_ru"),
                                          ("onepager_upload_en",
                                           "onepager_upload_ru"),)}),
                 ("Блок Subscribe", {"classes": ("collapse",),
                                     "fields": ((#"subscribe_blue_text",
                                                 "subscribe_blue_text_en",
                                                 "subscribe_blue_text_ru"),
                                                ("subscribe_white_text_en",
                                                 "subscribe_white_text_ru"),
                                                ("subscribe_title_en",
                                                 "subscribe_title_ru"))}),
                 ("Блок About", {"classes": ("collapse",),
                                 "fields": (("left_block1_title_en",
                                             "left_block1_title_ru"),
                                            ("left_block1_text_en",
                                             "left_block1_text_ru"),
                                            ("left_block2_title_en",
                                             "left_block2_title_ru"),
                                            ("left_block2_text_en",
                                             "left_block2_text_ru"),
                                            ("left_block_img1",),
                                            ("right_block_title_en",
                                             "right_block_title_ru"),
                                            ("right_block1_text_en",
                                             "right_block1_text_ru"),
                                            ("right_block_img",
                                             "right_block_img2",
                                             "right_block_img3"),
                                            ("ruledbook_link_en",
                                             "ruledbook_link_ru"),
                                            )
                                 }
                  ),
                 ("Блок Видеозаписи", {"classes": ("collapse",),
                                       "fields": (("video1_descr_en",
                                                   "video1_descr_ru"),
                                                  ("video1_link"),
                                                  ("video2_descr_en",
                                                   "video2_descr_ru"),
                                                  ("video2_link"),
                                            )
                                 }
                  ),
                 ("Блок Sale", {"classes": ("collapse",),
                                "fields": (("emission_sale_title_en",
                                            "emission_sale_title_ru"),
                                           ("emission_sale_text_en",
                                            "emission_sale_text_ru"),
                                           ("presale_1",
                                            "presale_2",
                                            "presale_3",
                                            "presale_4"),
                                           ("ico_1",
                                            "ico_2",
                                            "ico_3",
                                            "ico_4"),
                                           ("sale_bonus_title_en",
                                            "sale_bonus_title_ru"),
                                           ("sale_bonus_text_en",
                                            "sale_bonus_text_ru"),
                                           ("diagram_img_en",
                                            "diagram_img_ru"),
                                           )
                                }
                  ),
                 ("Блок Bounty and referal", {
                    "classes": ("collapse",),
                    "fields": (("bounty_title_en",
                                "bounty_title_ru"),
                               ("bounty_btn_text_en",
                                "bounty_btn_text_ru"),
                               ("bounty_text_en",
                                "bounty_text_ru"),
                               ("bounty_link",),
                               )
                 }
                 ),
                 ("Publication title", {
                    "classes": ("collapse",),
                    "fields": (("publication_block_title_en",
                                "publication_block_title_ru"),
                               )
                  }
                 ),
                 ("Exhibition title", {
                    "classes": ("collapse",),
                    "fields": (("exhibition_block_title_en",
                                "exhibition_block_title_ru"),
                               )
                  }
                 ),
                 ("Блок Funds chart", {"classes": ("collapse",),
                                       "fields": (("funds_title_en",
                                                   "funds_title_ru"),
                                                  ("funds_percent1",
                                                   "funds_text1_en",
                                                   "funds_text1_ru"),
                                                  ("funds_percent2",
                                                   "funds_text2_en",
                                                   "funds_text2_ru"),
                                                  ("funds_percent3",
                                                   "funds_text3_en",
                                                   "funds_text3_ru"),
                                                  ("funds_percent4",
                                                   "funds_text4_en",
                                                   "funds_text4_ru"),
                                                  ("funds_percent5",
                                                   "funds_text5_en",
                                                   "funds_text5_ru"),
                                                  ("funds_percent6",
                                                   "funds_text6_en",
                                                   "funds_text6_ru"),
                                                  ("funds_percent7",
                                                   "funds_text7_en",
                                                   "funds_text7_ru"),
                                                  ("funds_percent8",
                                                   "funds_text8_en",
                                                   "funds_text8_ru"),
                                                  )
                                       }
                  ),
                 ("Блок Tokens chart", {"classes": ("collapse",),
                                        "fields": (("tokens_title_en",
                                                    "tokens_title_ru"),
                                                   ("tokens_percent1",
                                                    "tokens_text1_en",
                                                    "tokens_text1_ru"),
                                                   ("tokens_percent2",
                                                    "tokens_text2_en",
                                                    "tokens_text2_ru"),
                                                   ("tokens_percent3",
                                                    "tokens_text3_en",
                                                    "tokens_text3_ru"),
                                                   ("tokens_percent4",
                                                    "tokens_text4_en",
                                                    "tokens_text4_ru"),
                                                   ("tokens_percent5",
                                                    "tokens_text5_en",
                                                    "tokens_text5_ru"),
                                                  )
                                       }
                  ),
                 ("Блок Socials", {"classes": ("collapse",),
                                   "fields": (("facebook",
                                               "medium",
                                               "linkedin",
                                               "reddit",
                                               "telegram",
                                               "bitcointalk",
                                               "twitter",
                                               "instagram"),
                                              )
                                   }
                  ),
                 )

    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }


@admin.register(Teammate)
class TeammateAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": (
            ('name_en',
             'name_ru'),
            ('position_en',
             'position_ru'),
            ('photo'),
            ('linkedin')
        )
        }
        ),
    )


@admin.register(Adviser)
class AdviserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": (
            ('name_en',
             'name_ru'),
            ('position_en',
             'position_ru'),
            ('photo'),
            ('linkedin')
        )
        }
        ),
    )


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": (
            ('title_en',
             'title_ru'),
            ('announce_en',
             'announce_ru'),
            ('image'),
            ('link')
        )
        }
        ),
    )


@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": (
            ('title_en',
             'title_ru'),
            ('announce_en',
             'announce_ru'),
            ('image'),
            ('link')
        )
        }
        ),
    )


@admin.register(AnswerQuestion)
class AnswerQuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": (
            ('question_en',
             'question_ru'),
            ('answer_en',
             'answer_ru')
        )
        }
        ),
    )


@admin.register(LandingConfiguration2)
class LandingConfiguration2Admin(SingletonModelAdmin):
    fieldsets = (("Блок Emission", {"classes": ("collapse",),
                                    "fields": (("emission_title_en",
                                                "emission_title_ru"),
                                               ("emission_text_en",
                                                "emission_text_ru"),
                                               ("emission_text_right_en",
                                                "emission_text_right_ru"),
                                               ("token_presale_title_en",
                                                "token_presale_title_ru"),
                                               ("token_presale_text_en",
                                                "token_presale_text_ru"),
                                               ("token_sale_title_en",
                                                "token_sale_title_ru"),
                                               ("token_sale_text_en",
                                                "token_sale_text_ru"),
                                           )}),
                 ("Блок Smart contract", {"classes": ("collapse",),
                                          "fields": (("contract_link",),
                                           )}),
                 ("Блок Exchange", {"classes": ("collapse",),
                                    "fields": (("about_top_text_en",
                                                "about_top_text_ru"),
                                               ("about_analytics_text_en",
                                                "about_analytics_text_ru"),
                                               ("about_indices_text_en",
                                                "about_indices_text_ru"),
                                               ("about_exchange_text_en",
                                                "about_exchange_text_ru"),
                                               ("about_bottom_text_en",
                                                "about_bottom_text_ru"),
                                               ("trading_link",)
                                               )
                                    }
                  ),
                 ("Заголовки блока 'Team'", {
                    "classes": ("collapse",),
                    "fields": (("team_title_en",
                                "team_title_ru"),
                               ("adviser_title_en",
                                "adviser_title_ru")
                               )
                  }
                 ),
                 ("Блок Бонусов", {"classes": ("collapse",),
                                   "fields": (("bar1_total",
                                               "bar1_bonus",
                                               "bar1_price"),
                                              ("bar2_total",
                                               "bar2_bonus",
                                               "bar2_price"),
                                              ("bar3_total",
                                               "bar3_bonus",
                                               "bar3_price"),
                                              ("bar4_total",
                                               "bar4_bonus",
                                               "bar4_price"),
                                              ("bar5_total",
                                               "bar5_bonus",
                                               "bar5_price"),
                                               )
                                    }
                  ),
                 ("Блок Roadmap", {"classes": ("collapse",),
                                   "fields": (("road_date1_en",
                                               "road_date1_ru",
                                               "road_text1_en",
                                               "road_text1_ru"),
                                              ("road_date2_en",
                                               "road_date2_ru",
                                               "road_text2_en",
                                               "road_text2_ru"),
                                              ("road_date3_en",
                                               "road_date3_ru",
                                               "road_text3_en",
                                               "road_text3_ru"),
                                              ("road_date4_en",
                                               "road_date4_ru",
                                               "road_text4_en",
                                               "road_text4_ru"),
                                              ("road_date5_en",
                                               "road_date5_ru",
                                               "road_text5_en",
                                               "road_text5_ru"),
                                              ("road_date6_en",
                                               "road_date6_ru",
                                               "road_text6_en",
                                               "road_text6_ru"),
                                              ("road_date7_en",
                                               "road_date7_ru",
                                               "road_text7_en",
                                               "road_text7_ru"),
                                              ("road_date8_en",
                                               "road_date8_ru",
                                               "road_text8_en",
                                               "road_text8_ru"),
                                              ("road_date9_en",
                                               "road_date9_ru",
                                               "road_text9_en",
                                               "road_text9_ru"),
                                              ("road_date10_en",
                                               "road_date10_ru",
                                               "road_text10_en",
                                               "road_text10_ru"),
                                              ("road_date11_en",
                                               "road_date11_ru",
                                               "road_text11_en",
                                               "road_text11_ru"),
                                              ("road_date12_en",
                                               "road_date12_ru",
                                               "road_text12_en",
                                               "road_text12_ru"),
                                               )
                                    }
                  ),
                 ("Блок Bounty page", {"classes": ("collapse",),
                                        "fields": (("bounty_subtitle_en",
                                                    "bounty_subtitle_ru"),
                                                   # ("facebook_link",
                                                   #  "referral_link",
                                                   #  "twitter_link",
                                                   #  "reddit_link",
                                                   #  "bitcoin_talk_link",
                                                   #  "media_link",
                                                   #  "medium_link",
                                                   #  "telegram_link",
                                                   #  "community_link",
                                                   #  "blogging_link",
                                                   #  "youtube_link",
                                                   #  "instagram_link",
                                                   #  "token_market_link"),
                                               )
                                    }
                  ),
                 ("Token sale terms", {"classes": ("collapse",),
                                       "fields": (("token_sale_terms_en",
                                                   "token_sale_terms_ru"),
                                               )
                                    }
                  ),
                 )


@admin.register(LandingConfiguration3)
class LandingConfiguration3Admin(SingletonModelAdmin):
    fieldsets = ((None, {"fields": ("discount_rate",
                                    ("donation_guide_doc_en",
                                     "donation_guide_doc_ru"),
                                    ("donation_guide_video_en",
                                     "donation_guide_video_ru"),
                                    ("presentation_text_en",
                                     "presentation_text_ru"),
                                     "presentation_link")}),
                 ("Rulebook", {"classes": ("collapse",),
                                    "fields": (("rulebook_en",
                                                "rulebook_ru"),
                                           )}),
                 ("Заголовки страниц", {"classes": ("collapse",),
                                        "fields": (("title_landing_en",
                                                    "title_landing_ru"),
                                                   ("title_lk_en",
                                                    "title_lk_ru"),
                                                   ("title_bounty_en",
                                                    "title_bounty_ru"),
                                           )}),
                 ("Mockups", {"classes": ("collapse",),
                                    "fields": (("mockup_en",
                                                "mockup_ru"),
                                           )}),
                 ("BOUNTY texts", {"classes": ("collapse",),
                                    "fields": (("facebook_bounty_title_en",
                                                "facebook_bounty_title_ru",
                                                "facebook_bounty_text_en",
                                                "facebook_bounty_text_ru"),
                                               ("twitter_bounty_title_en",
                                                "twitter_bounty_title_ru",
                                                "twitter_bounty_text_en",
                                                "twitter_bounty_text_ru"),
                                               ("referral_bounty_title_en",
                                                "referral_bounty_title_ru",
                                                "referral_bounty_text_en",
                                                "referral_bounty_text_ru"),
                                               ("media_bounty_title_en",
                                                "media_bounty_title_ru",
                                                "media_bounty_text_en",
                                                "media_bounty_text_ru"),
                                               ("btalk_bounty_title_en",
                                                "btalk_bounty_title_ru",
                                                "btalk_bounty_text_en",
                                                "btalk_bounty_text_ru"),
                                               ("reddit_bounty_title_en",
                                                "reddit_bounty_title_ru",
                                                "reddit_bounty_text_en",
                                                "reddit_bounty_text_ru"),
                                               ("community_bounty_title_en",
                                                "community_bounty_title_ru",
                                                "community_bounty_text_en",
                                                "community_bounty_text_ru"),
                                               ("telegram_bounty_title_en",
                                                "telegram_bounty_title_ru",
                                                "telegram_bounty_text_en",
                                                "telegram_bounty_text_ru"),
                                               ("linkedin_bounty_title_en",
                                                "linkedin_bounty_title_ru",
                                                "linkedin_bounty_text_en",
                                                "linkedin_bounty_text_ru"),
                                               ("tokenmarket_bounty_title_en",
                                                "tokenmarket_bounty_title_ru",
                                                "tokenmarket_bounty_text_en",
                                                "tokenmarket_bounty_text_ru"),
                                               ("youtube_bounty_title_en",
                                                "youtube_bounty_title_ru",
                                                "youtube_bounty_text_en",
                                                "youtube_bounty_text_ru"),
                                               ("blogging_bounty_title_en",
                                                "blogging_bounty_title_ru",
                                                "blogging_bounty_text_en",
                                                "blogging_bounty_text_ru"),
                                               ("instagram_bounty_title_en",
                                                "instagram_bounty_title_ru",
                                                "instagram_bounty_text_en",
                                                "instagram_bounty_text_ru"),
                                               ("more_bounty_title_en",
                                                "more_bounty_title_ru",
                                                "more_bounty_text_en",
                                                "more_bounty_text_ru"),
                                               ("bounty_top_text_en",
                                                "bounty_top_text_ru")
                                           )}),
                 ("Заголовки Rated by и Partners", {"classes": ("collapse",),
                                                    "fields": (("ratedby_block_title_en",
                                                                "ratedby_block_title_ru"),
                                                               ("partners_block_title_en",
                                                                "partners_block_title_ru")
                                           )}),
                 )


class FooterMenuItemInline(admin.StackedInline):
    model = FooterMenuItem
    extra = 1
    fields = ('name_en', 'name_ru', 'link_en', 'link_ru', 'open_new_tab')


@admin.register(FooterMenuCategory)
class FooterMenuCategoryAdmin(admin.ModelAdmin):
    inlines = (FooterMenuItemInline, )
    fields = ('name_en', 'name_ru', 'order')


# @admin.register(DonationAddresses)
# class DonationAddressesAdmin(SingletonModelAdmin):
#     pass


@admin.register(DonationAddress)
class DonationAddressAdmin(admin.ModelAdmin):
    pass


@admin.register(SaleStages)
class SaleStagesAdmin(SingletonModelAdmin):
    fieldsets = ((None, {"fields": (
                            ('show_before_stage',
                             'show_stage',
                             'show_end_stage'),
                            )}
                  ),
                 ("ДО НАЧАЛА ПРОДАЖ", {"classes": ("collapse",),
                                    "fields": (("before_start_title_en",
                                                "before_start_title_ru"),
                                               ("before_start_timer",),
                  )}),
                 ("В ПЕРИОД PRE-SALE/SALE", {"classes": ("collapse",),
                                          "fields": (("stage_title_en",
                                                      "stage_title_ru"),
                                                     ("stage_timer",),
                                                     ("stage_show_reised",
                                                      "stage_reised_text_en",
                                                      "stage_reised_text_ru",
                                                      "stage_reised_value"),
                                                     ("stage_show_bottom_btn",
                                                      "stage_bottom_btn_en",
                                                      "stage_bottom_btn_ru")
                  )}),
                 ("ПОСЛЕ PRE-SALE/SALE", {"classes": ("collapse",),
                                          "fields": (("end_title_en",
                                                      "end_title_ru"),
                                                     ("end_subtitle_en",
                                                      "end_subtitle_ru"),
                                                     ("end_show_reised",
                                                      "end_reised_text_en",
                                                      "end_reised_text_ru",
                                                      "end_reised_value"),
                                                     ("end_show_bottom_btn",
                                                      "end_bottom_btn_en",
                                                      "end_bottom_btn_ru")
                   )}),
                 )


class CrowdsaleCurrencyIndexInline(admin.StackedInline):
    model = CrowdsaleCurrencyIndex
    extra = 1
    fields = ('show_currency', 'image', 'name_en', 'name_ru', 'value', 'order')


@admin.register(CrowdsaleInfo)
class CrowdsaleInfoAdmin(SingletonModelAdmin):
    inlines = (CrowdsaleCurrencyIndexInline, )
    fields = ('title_en',
              'title_ru',
              'total_text_en',
              'total_text_ru',
              'total_value')


@admin.register(RatedBy)
class RatedByAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": (
            ('name_en',
             'name_ru'),
            ('image',),
            ('displayed',),
            ('link',)
        )
        }
        ),
    )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": (
            ('name_en',
             'name_ru'),
            ('image',),
            ('displayed',),
            ('link',)
        )
        }
        ),
    )


@admin.register(LandingPhoto)
class LandingPhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailConfig)
class EmailConfigAdmin(SingletonModelAdmin):
    fields = ('default_from_email',
              ('subscribe_subject_en',
               'subscribe_subject_ru',
               'subscribe_text_en',
               'subscribe_text_ru'),
              ('register_subject_en',
               'register_subject_ru',
               'register_text_en',
               'register_text_ru')
              )


@admin.register(PressKit)
class PressKitAdmin(SingletonModelAdmin):
    fields = ('show_preview',
              'show_download',
              ('preview_btn_text_en',
               'preview_btn_text_ru',
               'preview_btn_link'),
              ('download_btn_text_en',
               'download_btn_text_ru',
               'download_btn_link')
              )


@admin.register(ReferralSettings)
class ReferralSettingsAdmin(SingletonModelAdmin):
    fields = ('email',
              ('referral_terms_en',
               'referral_terms_ru'),
              ('advertisement_en',
               'advertisement_ru')
              )
