import threading

import mailchimp

from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _

from config.models import EmailConfig


def send_subscribe_notification(customer_email):
    email_config = EmailConfig.get_solo()
    html_body = render_to_string(
        "email/subscription.html",
        {
            "message": email_config.subscribe_text
        }
    )
    subject = email_config.subscribe_subject
    mail = EmailMultiAlternatives(
        subject,
        '',
        "ZNAQ {}".format(email_config.default_from_email),
        [customer_email,]
    )
    mail.attach_alternative(html_body, "text/html")
    mail.send()


class SendSubscribeMail(object):
    def __init__(self, email):
        self.email = email
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        # API_KEY = settings.MAILCHIMP_API_KEY
        # LIST_ID = settings.MAILCHIMP_SUBSCRIBE_LIST_ID
        # api = mailchimp.Mailchimp(API_KEY)
        # try:
        #     api.lists.subscribe(LIST_ID, {'email': self.email})
        # except Exception as e:
        #     print e
        #     return False

        send_subscribe_notification(self.email)


class UnsubscribeProcess(object):
    def __init__(self, email):
        self.email = email
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        API_KEY = settings.MAILCHIMP_API_KEY
        LIST_ID = settings.MAILCHIMP_SUBSCRIBE_LIST_ID
        api = mailchimp.Mailchimp(API_KEY)
        try:
            api.lists.unsubscribe(LIST_ID, {'email': self.email})
        except Exception as e:
            print e
            return False
