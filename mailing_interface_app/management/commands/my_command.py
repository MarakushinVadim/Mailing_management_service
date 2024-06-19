import smtplib
from datetime import datetime, timedelta

import pytz
from django.core.mail import send_mail

from Mailing_management_service import settings
import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from mailing_interface_app.models import SendingMailSet, SendTry

logger = logging.getLogger(__name__)


def my_job():
    print('1')

    def send_mailing():
        zone = pytz.timezone(settings.TIME_ZONE)
        current_datetime = datetime.now(zone)

        mailings = SendingMailSet.objects.all()
        try_time = datetime.now(zone) + timedelta(0, 9)

        for mailing in mailings:
            if mailing.next_sending_time > current_datetime and current_datetime < try_time:
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
                        next_sending_time = datetime.now(zone) + timedelta(1, 0)
                    elif mailing.sending_period == 'one_in_week':
                        next_sending_time = datetime.now(zone) + timedelta(7, 0)
                    else:
                        next_sending_time = datetime.now(zone) + timedelta(30, 0)
                    mailing.next_sending_time = next_sending_time

                    mailing.save()

                except smtplib.SMTPException:
                    SendTry.objects.create(sending_mail=mailing, status='FAILURE',
                                           last_sending_date=datetime.now())
                    mailing.sending_status = 'running'

                    mailing.next_sending_time = datetime.now(zone) + timedelta(0, 9)

                    mailing.save()

    send_mailing()


# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after your job has run. You should use it
# to wrap any jobs that you schedule that access the Django database in any way.
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),  # Every 10 seconds
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")

# class Command(BaseCommand):
#     help = 'Runs APS scheduler'
#
#     def handle(self, *args, **options):
#         scheduler = BackgroundScheduler()
#         scheduler.add_job(DjangoJobStore(), "default")
#         scheduler.add_job(print_hello, 'interval', seconds=10)
#
#
#
#
#
#
#
# # Функция старта периодических задач
# def start():
#     scheduler = BackgroundScheduler()
#
#     scheduler.start()
#
#
# def print_hello():
#     print('hello')
#
# def send_mailing():
#     zone = pytz.timezone(settings.TIME_ZONE)
#     current_datetime = datetime.now(zone)
#     # создание объекта с применением фильтра
#
#     send_mail(
#         subject='test',
#         message='test',
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=['marakushin.vadim@g,mail.com',]
#     )
#
#
# start()
