from modeltranslation.translator import translator, TranslationOptions

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
                     SaleStages,
                     CrowdsaleInfo,
                     CrowdsaleCurrencyIndex,
                     RatedBy,
                     Partner,
                     EmailConfig,
                     PressKit,
                     ReferralSettings)


class LandingConfigurationTranslationOptions(TranslationOptions):
    fields = ('timer_title',
              # 'raised_text',
              'sale_btn',
              'discount_info',
              'discount_end',
              'whitepaper_link',
              'whitepaper_upload',
              'onepager_link',
              'onepager_upload',
              'subscribe_blue_text',
              'subscribe_white_text',
              'subscribe_title',
              'left_block1_title',
              'left_block1_text',
              'left_block2_title',
              'left_block2_text',
              # 'left_block_img1_title',
              # 'left_block_img2_title',
              'right_block_title',
              'right_block1_text',
              # 'right_block2_text',
              # 'exchange_title',
              # 'exchange_descr',
              # 'exchange_triangle_text1',
              # 'exchange_triangle_text2',
              # 'exchange_triangle_text3',
              # 'exchange_triangle_text4',
              'funds_title',
              'funds_text1',
              'funds_text2',
              'funds_text3',
              'funds_text4',
              'funds_text5',
              'funds_text6',
              'funds_text7',
              'funds_text8',
              'tokens_title',
              'tokens_text1',
              'tokens_text2',
              'tokens_text3',
              'tokens_text4',
              'tokens_text5',
              'bounty_title',
              'bounty_btn_text',
              'bounty_text',
              'publication_block_title',
              'exhibition_block_title',
              'emission_sale_title',
              'emission_sale_text',
              'sale_bonus_title',
              'sale_bonus_text',
              'diagram_img',
              # 'emission_title',
              # 'emission_text',
              # 'token_presale_title',
              # 'token_presale_text',
              # 'token_sale_title',
              # 'token_sale_text'
              'ruledbook_link',
              'video1_descr',
              'video2_descr'
              )


class LandingConfiguration2TranslationOptions(TranslationOptions):
    fields = ('emission_title',
              'emission_text',
              'emission_text_right',
              'token_presale_title',
              'token_presale_text',
              'token_sale_title',
              'token_sale_text',
              'about_top_text',
              'about_analytics_text',
              'about_indices_text',
              'about_exchange_text',
              'about_bottom_text',
              'team_title',
              'adviser_title',
              'road_date1',
              'road_text1',
              'road_date2',
              'road_text2',
              'road_date3',
              'road_text3',
              'road_date4',
              'road_text4',
              'road_date5',
              'road_text5',
              'road_date6',
              'road_text6',
              'road_date7',
              'road_text7',
              'road_date8',
              'road_text8',
              'road_date9',
              'road_text9',
              'road_date10',
              'road_text10',
              'road_date11',
              'road_text11',
              'road_date12',
              'road_text12',
              'bounty_subtitle',
              'token_sale_terms'
              )


class LandingConfiguration3TranslationOptions(TranslationOptions):
    fields = ('rulebook',
              'title_landing',
              'title_lk',
              'title_bounty',
              'mockup',

              'facebook_bounty_title',
              'facebook_bounty_text',
              'referral_bounty_title',
              'referral_bounty_text',
              'twitter_bounty_title',
              'twitter_bounty_text',
              'reddit_bounty_title',
              'reddit_bounty_text',
              'btalk_bounty_title',
              'btalk_bounty_text',
              'media_bounty_title',
              'media_bounty_text',
              'linkedin_bounty_title',
              'linkedin_bounty_text',
              'telegram_bounty_title',
              'telegram_bounty_text',
              'community_bounty_title',
              'community_bounty_text',
              'blogging_bounty_title',
              'blogging_bounty_text',
              'youtube_bounty_title',
              'youtube_bounty_text',
              'tokenmarket_bounty_title',
              'tokenmarket_bounty_text',
              'instagram_bounty_title',
              'instagram_bounty_text',

              'more_bounty_title',
              'more_bounty_text',

              'ratedby_block_title',
              'partners_block_title',

              'bounty_top_text',
              'donation_guide_video',
              'donation_guide_doc',

              'presentation_text'
              )


class TeammateTranslationOptions(TranslationOptions):
    fields = ('name', 'position')


class AdviserTranslationOptions(TranslationOptions):
    fields = ('name', 'position')


class PublicationTranslationOptions(TranslationOptions):
    fields = ('title', 'announce')


class ExhibitionTranslationOptions(TranslationOptions):
    fields = ('title', 'announce')


class AnswerQuestionTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


class FooterMenuCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


class FooterMenuItemTranslationOptions(TranslationOptions):
    fields = ('name', 'link')


class SaleStagesTranslationOptions(TranslationOptions):
  fields = ('before_start_title',
            'stage_title',
            'stage_reised_text',
            'stage_bottom_btn',
            'end_title',
            'end_subtitle',
            'end_reised_text',
            'end_bottom_btn')


class CrowdsaleInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'total_text')


class CrowdsaleCurrencyIndexTranslationOptions(TranslationOptions):
    fields = ('name',)


class PartnerTranslationOptions(TranslationOptions):
    fields = ('name',)


class RatedByTranslationOptions(TranslationOptions):
    fields = ('name',)


class EmailConfigTranslationOptions(TranslationOptions):
    fields = ('subscribe_subject',
              'subscribe_text',
              'register_subject',
              'register_text')


class PressKitTranslationOptions(TranslationOptions):
    fields = ('preview_btn_text',
              'download_btn_text',)


class ReferralSettingsTranslationOptions(TranslationOptions):
    fields = ('referral_terms',
              'advertisement',)


translator.register(LandingConfiguration, LandingConfigurationTranslationOptions)
translator.register(LandingConfiguration2, LandingConfiguration2TranslationOptions)
translator.register(LandingConfiguration3, LandingConfiguration3TranslationOptions)
translator.register(Teammate, TeammateTranslationOptions)
translator.register(Adviser, AdviserTranslationOptions)
translator.register(Publication, PublicationTranslationOptions)
translator.register(Exhibition, ExhibitionTranslationOptions)
translator.register(AnswerQuestion, AnswerQuestionTranslationOptions)
translator.register(FooterMenuCategory, FooterMenuCategoryTranslationOptions)
translator.register(FooterMenuItem, FooterMenuItemTranslationOptions)
translator.register(SaleStages, SaleStagesTranslationOptions)
translator.register(CrowdsaleInfo, CrowdsaleInfoTranslationOptions)
translator.register(CrowdsaleCurrencyIndex, CrowdsaleCurrencyIndexTranslationOptions)
translator.register(Partner, PartnerTranslationOptions)
translator.register(RatedBy, RatedByTranslationOptions)
translator.register(EmailConfig, EmailConfigTranslationOptions)
translator.register(PressKit, PressKitTranslationOptions)
translator.register(ReferralSettings, ReferralSettingsTranslationOptions)
