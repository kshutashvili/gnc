# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

import os

from solo.models import SingletonModel
from ckeditor.fields import RichTextField

from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from django.core.files.storage import FileSystemStorage


class LandingConfiguration(SingletonModel):
    # block ICO (timer)
    timer_title = models.TextField(_("Заголовок для таймера"),
                                   default="До N-ной продажи токенов осталось:")
    timer_sale = models.DateTimeField(_("Таймер"),
                                      default='2017-12-31')
    # raised_text = models.CharField(_("Текст 'Собрано'"),
    #                                max_length=32,
    #                                default="Собрано")
    # raised_value = models.CharField(_("Значение 'Собрано'"),
    #                                 max_length=32,
    #                                 help_text=_("$10 929 925"))
    sale_btn = models.TextField(_("Название кнопки под таймером"),
                                default="НАШИ\nАКЦИИ",
                                max_length=32)

    # block ICO (discount)
    discount_info = models.TextField(_("Текст перед скидкой"),
                                     max_length=32,
                                     default="Текущая скидка:")
    discount = models.TextField(_("Размер скидки"),
                                max_length=10,
                                default='40%')
    discount_end = models.TextField(_("Текст после скидки"),
                                    max_length=32,
                                    default="Конец скидки:")
    discount_timer = models.DateTimeField(_("Таймер скидки"),
                                          default='2017-12-31')

    # whitepaper
    whitepaper_btn_text = models.TextField(_("Название кнопки whitepaper"),
                                           default="Whitepaper")
    whitepaper_link = models.TextField(_("Ссылка на whitepaper"),
                                       blank=True)
    whitepaper_upload = models.FileField(_("Загрузить whitepaper"),
                                         upload_to='whitepapers',
                                         blank=True)

    # onepager
    onepager_btn_text = models.TextField(_("Название кнопки onepager"),
                                         default="Onepager")
    onepager_link = models.TextField(_("Ссылка на onepager"),
                                     blank=True)
    onepager_upload = models.FileField(_("Загрузить onepager"),
                                       upload_to='onepagers',
                                       blank=True)

    # block subscribe
    subscribe_blue_text = models.TextField(_("Синий текст"),
                                           default="companyname")
    subscribe_white_text = models.TextField(_("Белый текст"),
                                            default="is a full-featured spot trading platform")
    subscribe_title = models.TextField(_("Заголовок формы"),
                                       default="ПОДПИШИСЬ НА НАШИ НОВОСТИ")

    # videos in header
    video1_link = models.TextField(_("Ссылка на первое видео с внешнего ресурса"),
                                   blank=True)
    video1_descr = models.TextField(_("Название первого видео"),
                                   blank=True)
    video2_link = models.TextField(_("Ссылка на второе видео с внешнего ресурса"),
                                   blank=True)
    video2_descr = models.TextField(_("Название второго видео"),
                                   blank=True)

    # block ABOUT
    left_block1_title = models.TextField(_("Заголовок первого блока слева"),
                                         blank=True,
                                         help_text='ZNAQ INDEX')
    left_block1_text = models.TextField(_("Текст первого блока слева"),
                                        blank=True)
    left_block2_title = models.TextField(_("Заголовок второго блока слева"),
                                         blank=True,
                                         help_text='ZNAQ TOKEN')
    left_block2_text = models.TextField(_("Текст второго блока слева"),
                                        blank=True)
    # left_block_img1_title = models.TextField(_("Заголовок первого изображения слева"),
    #                                          blank=True,
    #                                          help_text='INITIAL INVESTMENT')
    left_block_img1 = models.ImageField(_("Первое изображение для левого блока"),
                                        upload_to='landing_images',
                                        blank=True)
    # left_block_img2_title = models.TextField(_("Заголовок второго изображения слева"),
    #                                          blank=True,
    #                                          help_text='PURCHASE DATA')
    # left_block_img2 = models.ImageField(_("Второе изображение для левого блока"),
    #                                     upload_to='landing_images',
    #                                     blank=True)
    right_block_title = models.TextField(_("Заголовок блока справа"),
                                         blank=True,
                                         help_text='ОПИСАНИЕ РЫНКА КРИПТОВАЛЮТ')
    right_block1_text = models.TextField(_("Текст перовго блока справа"),
                                         blank=True)
    # right_block2_text = models.TextField(_("Текст второго блока справа"),
    #                                      blank=True)
    right_block_img = models.ImageField(_("Изображение для правого блока"),
                                        upload_to='landing_images',
                                        blank=True)
    right_block_img2 = models.ImageField(_("Второе изображение для правого блока"),
                                         upload_to='landing_images',
                                         blank=True)
    right_block_img3 = models.ImageField(_("Третье изображение для правого блока"),
                                         upload_to='landing_images',
                                         blank=True)
    ruledbook_link = models.TextField(_("Ссылка ruledbook"),
                                      default="#!")

    # block EXCHANGE
    # exchange_title = models.TextField(_("Заголовок блока 'exchange'"),
    #                                   blank=True)
    # exchange_descr = models.TextField(_("Текст блока 'exchange'"),
    #                                   blank=True)
    # exchange_triangle_text1 = models.TextField(_("Текст под первым треугольником"),
    #                                            blank=True)
    # exchange_triangle_text2 = models.TextField(_("Текст под вторым треугольником"),
    #                                            blank=True)
    # exchange_triangle_text3 = models.TextField(_("Текст под третьим треугольником"),
    #                                            blank=True)
    # exchange_triangle_text4 = models.TextField(_("Текст под четвёртым треугольником"),
    #                                            blank=True)

    # block takermaker funds
    funds_title = models.TextField(_("Заголовок блока 'Распределение средств'"),
                                   default="РАСПРЕДЕЛЕНИЕ СРЕДСТВ")
    funds_percent1 = models.CharField(_("Первое значение (%)"),
                                      max_length=10,
                                      default='6%')
    funds_text1 = models.TextField(_("Первое значение (текст)"),
                                   default="Операционные расходы")
    funds_percent2 = models.CharField(_("Второе значение (%)"),
                                      max_length=10,
                                      default='8%')
    funds_text2 = models.TextField(_("Второе значение (текст)"),
                                   default="Офисные расходы")
    funds_percent3 = models.CharField(_("Третье значение (%)"),
                                      max_length=10,
                                      default='20%')
    funds_text3 = models.TextField(_("Третье значение (текст)"),
                                   default="Биржа")
    funds_percent4 = models.CharField(_("Четвёртое значение (%)"),
                                      max_length=10,
                                      default='11%')
    funds_text4 = models.TextField(_("Четвёртое значение (текст)"),
                                   default="Маркетинг")
    funds_percent5 = models.CharField(_("Пятое значение (%)"),
                                      max_length=10,
                                      default='6%')
    funds_text5 = models.TextField(_("Пятое значение (текст)"),
                                   default="Юридические")
    funds_percent6 = models.CharField(_("Шестое значение (%)"),
                                      max_length=10,
                                      default='16%')
    funds_text6 = models.TextField(_("Шестое значение (текст)"),
                                   default="Запуск новых индексов")
    funds_percent7 = models.CharField(_("Седьмое значение (%)"),
                                      max_length=10,
                                      default='19%')
    funds_text7 = models.TextField(_("Седьмое значение (текст)"),
                                   default="Разработка единой системы торгов ZNAQ")
    funds_percent8 = models.CharField(_("Восьмое значение (%)"),
                                      max_length=10,
                                      default='14%')
    funds_text8 = models.TextField(_("Восьмое значение (текст)"),
                                   default="Аналитический клуб для владельцев ZNAQ Token")

    # block takermaker tokens
    tokens_title = models.TextField(_("Заголовок блока 'Распределение токенов'"),
                                    default="РАСПРЕДЕЛЕНИЕ ТОКЕНОВ")
    tokens_percent1 = models.CharField(_("Первое значение (%)"),
                                       max_length=10,
                                       default='60%')
    tokens_text1 = models.TextField(_("Первое значение (текст)"),
                                    default="ICO")
    tokens_percent2 = models.CharField(_("Второе значение (%)"),
                                       max_length=10,
                                       default='15%')
    tokens_text2 = models.TextField(_("Второе значение (текст)"),
                                    default="Команда")
    tokens_percent3 = models.CharField(_("Третье значение (%)"),
                                       max_length=10,
                                       default='10%')
    tokens_text3 = models.TextField(_("Третье значение (текст)"),
                                    default="Инвестора")
    tokens_percent4 = models.CharField(_("Четвёртое значение (%)"),
                                       max_length=10,
                                       default='10%')
    tokens_text4 = models.TextField(_("Четвёртое значение (текст)"),
                                    default="Маркетинг")
    tokens_percent5 = models.CharField(_("Пятое значение (%)"),
                                       max_length=10,
                                       default='5%')
    tokens_text5 = models.TextField(_("Пятое значение (текст)"),
                                    default="Баунти")

    # BOUNTY block
    bounty_title = models.TextField(_("Заголовок"),
                                    default="Баунти и реферальные прораммы")
    bounty_link = models.CharField(_("Bounty link"),
                                   max_length=64,
                                   default="#")
    bounty_btn_text = models.CharField(_("Название кнопки"),
                                       max_length=32,
                                       default="Перейти на страницу Баунти")
    bounty_text = models.TextField(_("Текст блока"),
                                   default="text")

    # PUBLICATIONS block
    publication_block_title = models.TextField(_("Заголовок блока 'Публикации'"),
                                               default="Публикации")

    # EXHIBITIONS block
    exhibition_block_title = models.TextField(_("Заголовок блока 'Exhibition'"),
                                              blank=True)

    # SOCIALS block
    facebook = models.CharField(_("Facebook"),
                                max_length=64,
                                blank=True)
    medium = models.CharField(_("Medium"),
                                max_length=64,
                                blank=True)
    linkedin = models.CharField(_("LinkedIn"),
                                max_length=64,
                                blank=True)
    reddit = models.CharField(_("Reddit"),
                                max_length=64,
                                blank=True)
    telegram = models.CharField(_("Telegram"),
                                max_length=64,
                                blank=True)
    bitcointalk = models.CharField(_("Bitcointalk"),
                                   max_length=64,
                                   blank=True)
    twitter = models.CharField(_("Twitter"),
                                max_length=64,
                                blank=True)
    instagram = models.CharField(_("Instagram"),
                                max_length=64,
                                blank=True)

    # SALES block
    emission_sale_title = models.TextField(_("Заголовок 'Скидка во время эмиссии'"),
                                           default="Скидки во время эмиссии")
    emission_sale_text = models.TextField(_("Текст под заголовком"),
                                          blank=True)
    presale_1 = models.IntegerField(_("Размер Presale скидки I промежутка"),
                                    default="50")
    presale_2 = models.IntegerField(_("Размер Presale скидки II промежутка"),
                                    default="45")
    presale_3 = models.IntegerField(_("Размер Presale скидки III промежутка"),
                                    default="40")
    presale_4 = models.IntegerField(_("Размер Presale скидки IV промежутка"),
                                    default="35")
    ico_1 = models.IntegerField(_("Размер ICO скидки I промежутка"),
                                default="30")
    ico_2 = models.IntegerField(_("Размер ICO скидки II промежутка"),
                                default="25")
    ico_3 = models.IntegerField(_("Размер ICO скидки III промежутка"),
                                default="20")
    ico_4 = models.IntegerField(_("Размер ICO скидки IV промежутка"),
                                default="15")
    sale_bonus_title = models.TextField(_("Заголовок 'Бонусы за размер платежа'"),
                                        default="Бонусы за размер платежа")
    sale_bonus_text = models.TextField(_("Текст под заголовком"),
                                       blank=True)
    diagram_img = models.ImageField(_("Диаграма скидок"),
                                    upload_to="sale_diagram",
                                    blank=True)

    class Meta:
        verbose_name = _("Конфигурация лэндинга")

    def __unicode__(self):
        return ugettext("Конфигурация лэндинга")


class LandingConfiguration2(SingletonModel):
    # EMISSION block
    emission_title = models.TextField(_("Заголовок"),
                                      default=_("Условия эмиссии"))
    emission_text = models.TextField(_("Текст под заголовком"),
                                     default=_("В период эмиссии..."))
    emission_text_right = models.TextField(_("Текст под заголовком (справа)"),
                                           default=_("В период эмиссии..."))

    token_presale_title = models.TextField(_("Заголовок TOKEN PRESALE"),
                                           default=_("Предпродажа токенов"))
    token_presale_text = RichTextField(_("Текст TOKEN PRESALE"),
                                       default=_("Start date..."))

    token_sale_title = models.TextField(_("Заголовок TOKEN SALE"),
                                        default=_("TOKEN SALE PHASE"))
    token_sale_text = RichTextField(_("Текст TOKEN SALE"),
                                    default="Start date...")

    # smart contract link
    contract_link = models.TextField(_("Ссылка на Smart contract"),
                                     default="#")

    # block ABOUT ZNAQ (exchange)
    about_top_text = models.TextField(_("Верхний текст"),
                                      blank=True)
    about_analytics_text = models.TextField(_("Текст 'Analytics'"),
                                            blank=True)
    about_indices_text = models.TextField(_("Текст 'Indices'"),
                                      blank=True)
    about_exchange_text = models.TextField(_("Текст 'Exchange'"),
                                      blank=True)
    about_bottom_text = models.TextField(_("Нижний текст"),
                                      blank=True)
    trading_link = models.TextField(_("Ссылка на Trading-платформу"),
                                    default="http://znaq.com/")

    # TEAM block title
    team_title = models.TextField(_("Заголовок блока 'Наша команда'"),
                                  default="Наша команда")

    # ADVISERS block title
    adviser_title = models.TextField(_("Заголовок блока 'Advisers'"),
                                     default="Адвайзеры")

    # BONUSES
    bar1_total = models.TextField(_("Итоговая сумма (1)"),
                                  default="52,25")
    bar1_bonus = models.TextField(_("Размер бонуса ZNAQ (1)"),
                                  default="+4,5%")
    bar1_price = models.TextField(_("Сума платежа (1)"),
                                  default="50")
    bar2_total = models.TextField(_("Итоговая сумма (2)"),
                                  default="78,55")
    bar2_bonus = models.TextField(_("Размер бонуса ZNAQ (2)"),
                                  default="+5%")
    bar2_price = models.TextField(_("Сума платежа (2)"),
                                  default="75")
    bar3_total = models.TextField(_("Итоговая сумма (3)"),
                                  default="105,5")
    bar3_bonus = models.TextField(_("Размер бонуса ZNAQ (3)"),
                                  default="+5,5%")
    bar3_price = models.TextField(_("Сума платежа (3)"),
                                  default="100")
    bar4_total = models.TextField(_("Итоговая сумма (4)"),
                                  default="159")
    bar4_bonus = models.TextField(_("Размер бонуса ZNAQ (4)"),
                                  default="+6%")
    bar4_price = models.TextField(_("Сума платежа (4)"),
                                  default="150")
    bar5_total = models.TextField(_("Итоговая сумма (5)"),
                                  default="213")
    bar5_bonus = models.TextField(_("Размер бонуса ZNAQ (5)"),
                                  default="+6,5%")
    bar5_price = models.TextField(_("Сума платежа (5)"),
                                  default="200")

    # ROADMAP
    road_date1 = models.TextField(_("Roadmap дата (1)"),
                                  blank=True)
    road_text1 = models.TextField(_("Roadmap текст (1)"),
                                  blank=True)
    road_date2 = models.TextField(_("Roadmap дата (2)"),
                                  blank=True)
    road_text2 = models.TextField(_("Roadmap текст (2)"),
                                  blank=True)
    road_date3 = models.TextField(_("Roadmap дата (3)"),
                                  blank=True)
    road_text3 = models.TextField(_("Roadmap текст (3)"),
                                  blank=True)
    road_date4 = models.TextField(_("Roadmap дата (4)"),
                                  blank=True)
    road_text4 = models.TextField(_("Roadmap текст (4)"),
                                  blank=True)
    road_date5 = models.TextField(_("Roadmap дата (5)"),
                                  blank=True)
    road_text5 = models.TextField(_("Roadmap текст (5)"),
                                  blank=True)
    road_date6 = models.TextField(_("Roadmap дата (6)"),
                                  blank=True)
    road_text6 = models.TextField(_("Roadmap текст (6)"),
                                  blank=True)
    road_date7 = models.TextField(_("Roadmap дата (7)"),
                                  blank=True)
    road_text7 = models.TextField(_("Roadmap текст (7)"),
                                  blank=True)
    road_date8 = models.TextField(_("Roadmap дата (8)"),
                                  blank=True)
    road_text8 = models.TextField(_("Roadmap текст (8)"),
                                  blank=True)
    road_date9 = models.TextField(_("Roadmap дата (9)"),
                                  blank=True)
    road_text9 = models.TextField(_("Roadmap текст (9)"),
                                  blank=True)
    road_date10 = models.TextField(_("Roadmap дата (10)"),
                                   blank=True)
    road_text10 = models.TextField(_("Roadmap текст (10)"),
                                   blank=True)
    road_date11 = models.TextField(_("Roadmap дата (11)"),
                                   blank=True)
    road_text11 = models.TextField(_("Roadmap текст (11)"),
                                   blank=True)
    road_date12 = models.TextField(_("Roadmap дата (12)"),
                                   blank=True)
    road_text12 = models.TextField(_("Roadmap текст (12)"),
                                   blank=True)

    # BOUNTY
    bounty_subtitle = models.TextField(_("Подзаголовок bounty page"),
                                       blank=True)
    facebook_link = models.TextField(_("Bounty facebook"),
                                     default='#')
    referral_link = models.TextField(_("Bounty referral"),
                                     default='#')
    twitter_link = models.TextField(_("Bounty twitter"),
                                    default='#')
    reddit_link = models.TextField(_("Bounty reddit"),
                                   default='#')
    bitcoin_talk_link = models.TextField(_("Bounty bitcoin talk"),
                                         default='#')
    media_link = models.TextField(_("Bounty media"),
                                  default='#')
    medium_link = models.TextField(_("Bounty medium"),
                                   default='#')
    telegram_link = models.TextField(_("Bounty telegram"),
                                     default='#')
    community_link = models.TextField(_("Bounty community"),
                                      default='#')
    blogging_link = models.TextField(_("Bounty blogging"),
                                     default='#')
    youtube_link = models.TextField(_("Bounty youtube"),
                                    default='#')
    token_market_link = models.TextField(_("Bounty token market"),
                                         default='#')
    instagram_link = models.TextField(_("Bounty instagram"),
                                      default='#')

    # token sale terms
    token_sale_terms = models.TextField(_("Token sale terms"),
                                        blank=True)

    class Meta:
        verbose_name = _("Конфигурация лэндинга ч.2")

    def __unicode__(self):
        return ugettext("Конфигурация лэндинга ч.2")

    def bonus_to_float(self, value):
        # "+5,5%" -> "5,5"
        splitted_bonus = value.split('%')[0].split("+")[1]
        if "," in splitted_bonus:
            up, down = splitted_bonus.split(",")
            # 5 and 5 -> 5.5
            return int(up) + int(down) / 10 ** len(str(down))
        return splitted_bonus


class LandingConfiguration3(SingletonModel):
    rulebook = models.FileField(_("Загрузить rulebook"),
                                       upload_to='rulebook',
                                       blank=True)
    title_landing = models.TextField(_("Заголовок лэндинга (в браузере)"),
                                     default="ZNAQ")
    title_lk = models.TextField(_("Заголовок личного кабинета (в браузере)"),
                                default="ZNAQ | Профиль")
    title_bounty = models.TextField(_("Заголовок баунти страницы (в браузере)"),
                                    default="ZNAQ | Баунти")

    # BOUNTY texts
    facebook_bounty_title = models.TextField(
        _("Facebook bounty modal title"),
        default='Facebook bounty'
    )
    facebook_bounty_text = RichTextField(
        _("Facebook bounty modal text"),
        default='To take part in the Facebook bounty campaign ...')

    referral_bounty_title = models.TextField(
        _("Referral bounty modal title"),
        default='Referral bounty'
    )
    referral_bounty_text = RichTextField(
        _("Referral bounty modal text"),
        default='To take part in the Referral bounty campaign ...')

    twitter_bounty_title = models.TextField(
        _("Twitter bounty modal title"),
        default='Twitter bounty'
    )
    twitter_bounty_text = RichTextField(
        _("Twitter bounty modal text"),
        default='To take part in the Twitter bounty campaign ...')

    reddit_bounty_title = models.TextField(
        _("Reddit bounty modal title"),
        default='Reddit bounty'
    )
    reddit_bounty_text = RichTextField(
        _("Reddit bounty modal text"),
        default='To take part in the Reddit bounty campaign ...')

    btalk_bounty_title = models.TextField(
        _("Bitcoin Talk bounty modal title"),
        default='Bitcoin Talk bounty'
    )
    btalk_bounty_text = RichTextField(
        _("Bitcoin Talk bounty modal text"),
        default='To take part in the Bitcoin Talk bounty campaign ...')

    media_bounty_title = models.TextField(
        _("Media bounty modal title"),
        default='Media bounty'
    )
    media_bounty_text = RichTextField(
        _("Media bounty modal text"),
        default='To take part in the Media bounty campaign ...')

    linkedin_bounty_title = models.TextField(
        _("LinkedIn bounty modal title"),
        default='LinkedIn bounty'
    )
    linkedin_bounty_text = RichTextField(
        _("LinkedIn bounty modal text"),
        default='To take part in the LinkedIn bounty campaign ...')

    telegram_bounty_title = models.TextField(
        _("Telegram bounty modal title"),
        default='Telegram bounty'
    )
    telegram_bounty_text = RichTextField(
        _("Telegram bounty modal text"),
        default='To take part in the Telegram bounty campaign ...')

    community_bounty_title = models.TextField(
        _("Community bounty modal title"),
        default='Community bounty'
    )
    community_bounty_text = RichTextField(
        _("Community bounty modal text"),
        default='To take part in the Community bounty campaign ...')

    blogging_bounty_title = models.TextField(
        _("Bloging & Vloging bounty modal title"),
        default='Bloging & Vloging bounty'
    )
    blogging_bounty_text = RichTextField(
        _("Bloging & Vloging bounty modal text"),
        default='To take part in the Bloging & Vloging bounty campaign ...')

    youtube_bounty_title = models.TextField(
        _("Youtube bounty modal title"),
        default='Youtube bounty'
    )
    youtube_bounty_text = RichTextField(
        _("Youtube bounty modal text"),
        default='To take part in the Youtube bounty campaign ...')

    tokenmarket_bounty_title = models.TextField(
        _("Token Market bounty modal title"),
        default='Token Market bounty'
    )
    tokenmarket_bounty_text = RichTextField(
        _("Token Market bounty modal text"),
        default='To take part in the Token Market bounty campaign ...')

    instagram_bounty_title = models.TextField(
        _("Instagram bounty modal title"),
        default='Instagram bounty'
    )
    instagram_bounty_text = RichTextField(
        _("Instagram bounty modal text"),
        default='To take part in the Instagram bounty campaign ...')

    more_bounty_title = models.TextField(
        _("More bounty modal title"),
        default='More title'
    )
    more_bounty_text = RichTextField(
        _("More bounty modal text"),
        default='More text...')

    bounty_top_text = models.TextField(_("Bounty page intro"),
                                       default='Intro')

    # mockups images
    mockup = models.ImageField(_("Mockup image"),
                               upload_to='mockups',
                               blank=True)

    # ratedby block
    ratedby_block_title = models.TextField(_("Заголовок блока Rated By"),
                                           default="Rated By")
    # partners
    partners_block_title = models.TextField(_("Заголовок блока Partners"),
                                            default="Partners")

    # discount rate for lk calc
    discount_rate = models.CharField(_("Коэффициент скидки для калькулятора"),
                                     default="1.4",
                                     max_length=32)

    donation_guide_doc = models.TextField(
        _("Ссылка на Инструкцию покупки токенов (ЛК)"),
        default="#"
    )
    donation_guide_video = models.TextField(
        _("Ссылка на Видео-инструкцию (ЛК)"),
        default="#"
    )

    presentation_text = models.TextField(_("Название кнопки Presentation"),
                                         default="Presentation")
    presentation_link = models.TextField(_("Ссылка на Presentation"),
                                         blank=True)

    class Meta:
        verbose_name = _("Конфигурация лэндинга ч.3")

    def __unicode__(self):
        return ugettext("Конфигурация лэндинга ч.3")


class Teammate(models.Model):
    photo = models.ImageField(_("Фото"),
                              upload_to="team")
    name = models.CharField(_("Имя"),
                            max_length=128)
    position = models.CharField(_("Роль в команде"),
                                max_length=128)
    linkedin = models.CharField(_("LinkedIn"),
                                max_length=128,
                                blank=True)

    class Meta:
        verbose_name = _("Сотрудник")
        verbose_name_plural = _("Сотрудники")

    def __unicode__(self):
        return self.name


class Adviser(models.Model):
    photo = models.ImageField(_("Фото"),
                              upload_to="adviser")
    name = models.CharField(_("Имя"),
                            max_length=128)
    position = models.CharField(_("Роль"),
                                max_length=128)
    linkedin = models.CharField(_("LinkedIn"),
                                max_length=128,
                                blank=True)

    class Meta:
        verbose_name = _("Adviser")
        verbose_name_plural = _("Adviser")

    def __unicode__(self):
        return self.name


class Publication(models.Model):
    image = models.ImageField(_("Изображение"),
                              upload_to="publication")
    title = models.TextField(_("Заголовок"))
    announce = models.TextField(_("Краткое описание"))
    link = models.CharField(_("Ссылка"),
                            max_length=128,
                            default="#")

    class Meta:
        verbose_name = _("Publication")
        verbose_name_plural = _("Publications")

    def __unicode__(self):
        return self.title


class Exhibition(models.Model):
    image = models.ImageField(_("Изображение"),
                              upload_to="exhibition")
    title = models.TextField(_("Заголовок"))
    announce = models.TextField(_("Краткое описание"),
                                blank=True)
    link = models.CharField(_("Ссылка"),
                            max_length=128,
                            default="#")

    class Meta:
        verbose_name = _("Exhibition")
        verbose_name_plural = _("Exhibitions")

    def __unicode__(self):
        return self.title


class AnswerQuestion(models.Model):
    question = models.TextField(_("Вопрос"),
                                max_length=128)
    answer = models.TextField(_("Ответ"))

    class Meta:
        verbose_name = _("Вопрос-Ответ")
        verbose_name_plural = _("Вопросы-Ответы")

    def __unicode__(self):
        return self.question


class FooterMenuCategory(models.Model):
    name = models.TextField(_("Название категории меню футера"),
                            max_length=128)
    order = models.IntegerField(_('Порядок'),
                                default=0)

    class Meta:
        verbose_name = _("Категория меню футера")
        verbose_name_plural = _("Категории меню футера")
        ordering = ['order', ]

    def __unicode__(self):
        return self.name


class FooterMenuItem(models.Model):
    category = models.ForeignKey(FooterMenuCategory,
                                 related_name="footer_items")
    name = models.TextField(_("Название ссылки"),
                            max_length=128)
    link = models.CharField(_("Ссылка"),
                            max_length=128)
    open_new_tab = models.BooleanField(_("Открывать в новой вкладке"),
                                       default=False)

    class Meta:
        verbose_name = _("Пункт меню футера")
        verbose_name_plural = _("Пункт меню футера")

    def __unicode__(self):
        return self.name


class DonationAddresses(SingletonModel):
    """
    Do not use this
    """
    eth_address = models.CharField(_("Адрес ETH"), max_length=50)
    btc_address = models.CharField(_("Адрес BTC"), max_length=50)
    ltc_address = models.CharField(_("Адрес LTC"), max_length=50)
    etc_address = models.CharField(_("Адрес ETC"), max_length=50)

    class Meta:
        verbose_name = _("Адреса для покупки токенов")

    def __unicode__(self):
        return ugettext("Адреса для покупки токенов")


class DonationAddress(models.Model):
    currency_name = models.CharField(_("Название Валюты"),
                                     unique=True,
                                     max_length=128,
                                     default='Ethereum',
                                     help_text='Bitcoin, Ripple etc.')
    currency = models.CharField(_("Сокращенное название валюты"),
                                unique=True,
                                max_length=12,
                                default='ETH',
                                help_text='BTC, ETH, LTC etc.')
    address = models.CharField(_("Адрес кошелька"),
                               max_length=128,
                               unique=True)

    class Meta:
        verbose_name = "Адрес для покупки токенов"
        verbose_name_plural = "Адреса для покупки токенов"

    def __unicode__(self):
        return "{} address".format(self.currency)


class SaleStages(SingletonModel):
    show_before_stage = models.BooleanField(_("Отображать блок до начала Presale/Sale стадий?"),
                                            default=True)
    show_stage = models.BooleanField(_("Отображать блок при Presale/Sale стадиях?"),
                                     default=False)
    show_end_stage = models.BooleanField(_("Отображать блок после завершения всех стадий?"),
                                         default=False)

    before_start_title = models.TextField(_("Текст-заголовок до начала Presale/Sale стадий"),
                                          default="До начала Pre-Sale осталось:")
    before_start_timer = models.DateTimeField(_("Таймер до начала Presale/Sale стадий"),
                                              default='2018-03-01')

    stage_title = models.TextField(_("Текст-заголовок при Presale/Sale стадиях"),
                                   default="До конца Pre-Sale осталось:")
    stage_timer = models.DateTimeField(_("Таймер до конца Presale/Sale стадий"),
                                       default='2018-03-01')
    stage_show_reised = models.BooleanField(_("Показывать Reised?"),
                                            default=True)
    stage_reised_text = models.CharField(_("Текст Reised/Собрано"),
                                         default="Reised",
                                         max_length=32)
    stage_reised_value = models.CharField(_("Количество собраных денег"),
                                          default="$ 10 357 456",
                                          max_length=32)
    stage_show_bottom_btn = models.BooleanField(_("Показывать кнопку показателей?"),
                                                default=True)
    stage_bottom_btn = models.TextField(_("Название кнопки под таймером"),
                                        default="показатели\nкраудсейла",
                                        max_length=32)

    end_title = models.TextField(_("Текст-заголовок после завершения всех стадий"),
                                 default="Pre-sale finished")
    end_subtitle = models.TextField(_("Подзаголовок после завершения всех стадий"),
                                    default="Thank you for your contribution")
    end_show_reised = models.BooleanField(_("Показывать Reised?"),
                                          default=True)
    end_reised_text = models.CharField(_("Текст Reised/Собрано"),
                                       default="Reised",
                                       max_length=32)
    end_reised_value = models.CharField(_("Количество собраных денег"),
                                        default="$ 10 357 456",
                                        max_length=32)
    end_show_bottom_btn = models.BooleanField(_("Показывать кнопку показателей?"),
                                              default=True)
    end_bottom_btn = models.TextField(_("Название кнопки под таймером"),
                                      default="показатели\nкраудсейла",
                                      max_length=32)

    class Meta:
        verbose_name = "Стадии проекта для header лендинга"

    def __unicode__(self):
        return ugettext("Стадии проекта для header лендинга")


class CrowdsaleInfo(SingletonModel):
    title = models.CharField(_("Заголовок поп-апа 'Показатели краудсейла'"),
                                   max_length=64,
                                   default="ПОКАЗАТЕЛИ КРАУДСЕЙЛА")
    total_text = models.CharField(_("Текст 'Total'"),
                                        max_length=32,
                                        default="Total")
    total_value = models.CharField(_("Значение 'Total'"),
                                         max_length=32,
                                         default="$ 11201")

    class Meta:
        verbose_name = "Поп-ап показателей краудсейла"

    def __unicode__(self):
        return ugettext("Поп-ап показателей краудсейла")


class CrowdsaleCurrencyIndexQuerySet(models.QuerySet):
    def show_currency(self, *args, **kwargs):
        kwargs['show_currency'] = True
        return self.filter(*args, **kwargs)

    def ordering(self):
        return self.order_by('order')


class CrowdsaleCurrencyIndex(models.Model):

    show_currency = models.BooleanField(_("Показывать этот пункт?"),
                                        default=True)
    image = models.ImageField(_("Изображение валюты"),
                              upload_to="crowdsale_img",
                              blank=True)
    name = models.CharField(_("Название пункта"),
                            max_length=64,
                            help_text="Bitcoin, Ripple, Другие инвестиции etc.")
    value = models.CharField(_("Значение"),
                             max_length=32,
                             help_text="Например: 1004 BTC")
    order = models.PositiveIntegerField(_("Порядок"),
                                        default=0)
    info = models.ForeignKey(CrowdsaleInfo,
                             blank=True,
                             null=True,
                             related_name="crowdsale_currencies")

    objects = CrowdsaleCurrencyIndexQuerySet.as_manager()

    class Meta:
        verbose_name = "Валюта для окна 'Показатели краудсейла'"
        verbose_name_plural = "Валюты для окна 'Показатели краудсейла'"

    def __unicode__(self):
        return self.name


class RatedAndPartnerQuerySet(models.QuerySet):
    def displayed(self, *args, **kwargs):
        kwargs['displayed'] = True
        return self.filter(*args, **kwargs)


class RatedBy(models.Model):
    name = models.CharField(_("Название/Текст"),
                            max_length=128,
                            blank=True)
    image = models.ImageField(_("Изображение"),
                              upload_to="rated_by")
    displayed = models.BooleanField(_("Отображать?"),
                                    default=True)
    link = models.CharField(_("Ссылка"),
                            max_length=128,
                            blank=True)

    objects = RatedAndPartnerQuerySet.as_manager()

    class Meta:
        verbose_name = "Rated by block item"
        verbose_name_plural = "Rated by block items"

    def __unicode__(self):
        return self.name or str(self.id)


class Partner(models.Model):
    name = models.CharField(_("Название/Текст"),
                            max_length=128,
                            blank=True)
    image = models.ImageField(_("Изображение"),
                              upload_to="partner")
    displayed = models.BooleanField(_("Отображать?"),
                                    default=True)
    link = models.CharField(_("Ссылка"),
                            max_length=128,
                            blank=True)

    objects = RatedAndPartnerQuerySet.as_manager()

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"

    def __unicode__(self):
        return self.name or str(self.id)


class CompressedImageField(models.ImageField):
    # from compability with old migration
    pass


class LandingPhotoQuerySet(models.QuerySet):
    def showed_photos(self, *args, **kwargs):
        kwargs['show'] = True
        return self.filter(*args, **kwargs)


class LandingPhoto(models.Model):
    image = models.ImageField("Photo",
                              upload_to="compressed")

    show = models.BooleanField("Отображать?",
                               default=True)

    objects = LandingPhotoQuerySet.as_manager()

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photo"

    def __unicode__(self):
        return self.image.name or str(self.id)


class EmailConfig(SingletonModel):
    default_from_email = models.CharField(
        _("Email с которого будут отсылаться оповещения"),
        default="noreply@example.com",
        max_length=64
    )

    subscribe_subject = models.TextField(
        _("Заголовок оповещения о подписке на новости"),
        default="ZNAQ News Subscription"
    )
    subscribe_text = RichTextField(
        _("Текст оповещения о подписке на новости"),
        default="You successfully subscribed!"
    )

    register_subject = models.TextField(
        _("Заголовок оповещения о регистрации на сайте"),
        default="ZNAQ Registration"
    )
    register_text = RichTextField(
        _("Текст оповещения о регистрации на сайте"),
        default="You successfully registered!"
    )

    class Meta:
        verbose_name = "Настройки email оповещений"

    def __unicode__(self):
        return ugettext("Настройки email оповещений")


class OverwriteStorage(FileSystemStorage):
    """
    Overwrite existing file with the name.
    """

    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(self.location, name))
        return super(OverwriteStorage, self).get_available_name(name, max_length)


class PressKit(SingletonModel):
    preview_btn_text = models.CharField(
        _("Текст кнопки Preview"),
        max_length=32,
        default="Preview"
    )
    preview_btn_link = models.URLField(
        _("Ссылка на Preview"),
        default='#'
    )
    show_preview = models.BooleanField(
        _("Отображать кнопку Preview"),
        default=True
    )

    download_btn_text = models.CharField(
        _("Текст кнопки Download"),
        max_length=32,
        default="Download"
    )
    download_btn_link = models.FileField(
        _("Архив для скачивания"),
        upload_to='press_kit',
        storage=OverwriteStorage()
    )
    show_download = models.BooleanField(
        _("Отображать кнопку Download"),
        default=True
    )

    class Meta:
        verbose_name = "Press Kit"

    def __unicode__(self):
        return ugettext("Press Kit")


class ReferralSettings(SingletonModel):
    referral_terms = RichTextField(
        _("Referral terms на реферальной странице"),
        default="Referral terms"
    )
    advertisement = RichTextField(
        _("Advertisement materials на реферальной странице"),
        default="Advertisement materials"
    )
    email = models.CharField(
        _("Email"),
        max_length=64,
        default="coop@znaq.org"
    )

    class Meta:
        verbose_name = "Referral Page Settings"

    def __unicode__(self):
        return ugettext("Referral Page Settings")
