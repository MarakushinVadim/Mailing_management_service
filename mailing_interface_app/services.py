from datetime import datetime
from smtplib import SMTPException

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from django.urls import reverse
from django.utils import timezone

from Mailing_management_service import settings
from mailing_interface_app.models import SendingMailSet, ClientService, SendTry








def send_email_to_all_clients(sending_mail_set):

    clients = ClientService.objects.filter(user=sending_mail_set.message.user)
    for client in clients:
        try:
            send_mail(
                subject=sending_mail_set.message.letter_subject,
                message=sending_mail_set.message.letter_text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email],
                fail_silently=False
            )
            SendTry.objects.crate(
                sending_mail=sending_mail_set,
                client=client,
                last_sending_date=timezone.now(),
                status = SendTry.StatusChoices.SUCCESS,
                server_response='Сообщение успешно отправлено'
            )
        except SMTPException as e:
            SendTry.objects.crate(
                sending_mail=sending_mail_set,
                client=client,
                last_sending_date=timezone.now(),
                status=SendTry.StatusChoices.FAILURE,
                server_response=str(e)
            )


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing, 'interval', minutes=1)
    scheduler.start()


def send_mailing( client):
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings = SendingMailSet.objects.filter(first_sending_date__lte=current_datetime).filter(sending_status=SendingMailSet.SendingStatusChoices.RUNNING)


    for mailing in mailings:
        send_mail(
                subject=mailing.message.letter_subject,
                message=mailing.message.letter_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.client_service.all()]
           )

