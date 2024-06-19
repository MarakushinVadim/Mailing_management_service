from datetime import datetime

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail

from Mailing_management_service import settings
from mailing_interface_app.models import SendingMailSet


# def send_mailing():
#     zone = pytz.timezone(settings.TIME_ZONE)
#     current_datetime = datetime.now(zone)
#     # создание объекта с применением фильтра
#     mailings = SendingMailSet.objects.filter(first_sending_date__lte=current_datetime).filter(
#         sending_status=SendingMailSet.SendingStatusChoices.RUNNING)
#
#     for mailing in mailings:
#         send_mail(
#             subject=mailing.message.letter_subject,
#             message=mailing.message.letter_body,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=["marakushin.vadim@gmail.com"]
#         )
