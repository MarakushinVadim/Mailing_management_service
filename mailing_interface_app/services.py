import smtplib
from datetime import datetime, timedelta

import pytz
from django.core.mail import send_mail

from Mailing_management_service import settings
from mailing_interface_app.models import SendingMailSet, SendTry


def my_job():
    print('1')

    def send_mailing():
        current_datetime = datetime.now(pytz.utc)

        mailings = SendingMailSet.objects.filter(next_sending_time__lte=current_datetime)


        for mailing in mailings:
            if mailing.sending_status != 'completed':
                mailing.sending_status = 'running'
                print(f'обьект SendingMailSet - {mailing.name}')
                try:
                    server_response = send_mail(
                        subject=mailing.message.letter_subject,
                        message=mailing.message.letter_body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email for client in mailing.client_service.all()],
                        fail_silently=False
                    )
                    SendTry.objects.create(sending_mail=mailing, status='SUCCESS',
                                           last_sending_date=datetime.now(), server_response=server_response)
                    mailing.sending_status = 'completed'

                    if mailing.sending_period == 'one_in_day':
                        next_sending_time = datetime.now(pytz.utc) + timedelta(1, 0)
                        mailing.next_sending_time = next_sending_time

                    elif mailing.sending_period == 'one_in_week':
                        next_sending_time = datetime.now(pytz.utc) + timedelta(7, 0)
                        mailing.next_sending_time = next_sending_time

                    else:
                        next_sending_time = datetime.now(pytz.utc) + timedelta(30, 0)
                        mailing.next_sending_time = next_sending_time

                    mailing.save()

                except smtplib.SMTPException:
                    SendTry.objects.create(sending_mail=mailing, status='FAILURE',
                                           last_sending_date=datetime.now())
                    mailing.sending_status = 'running'

                    mailing.save()

    send_mailing()


