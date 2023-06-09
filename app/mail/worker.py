from __future__ import absolute_import, unicode_literals

from datetime import datetime, timedelta
from typing import NoReturn

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from taikhoan.models import Taikhoan as User

from app.settings import EMAIL_HOST_USER


def mailing_healchecl(plugins):
    mail_subject = "Heal check report"
    html_message = render_to_string("mail/mail.html", {"plugins": plugins})

    message = EmailMessage(
        mail_subject, html_message, EMAIL_HOST_USER, [EMAIL_HOST_USER]
    )
    message.content_subtype = (
        "html"  # this is required because there is no plain text email message
    )
    message.send()


def report_user_daily() -> NoReturn:
    """Daily report for admin the number of registered users"""
    user_in_day = User.objects.filter(
        date_joined__gte=datetime.now() - timedelta(days=1)
    )

    mail_subject = "New user daily report"
    html_message = f"""
    <h1>New user daily report</h1>
    <p>There are {user_in_day.count()} user in the last 24h</p>
    <div>Detail:</div>
    <ul>
        {''.join([f'<li>{user.full_name()}</li>' for user in user_in_day])}

    """

    message = EmailMessage(
        mail_subject, html_message, EMAIL_HOST_USER, [EMAIL_HOST_USER]
    )
    message.content_subtype = (
        "html"  # this is required because there is no plain text email message
    )
    message.send()

    # return here
