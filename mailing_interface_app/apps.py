from time import sleep

from django.apps import AppConfig


class MailingInterfaceAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mailing_interface_app"

    def ready(self):
        from mailing_interface_app.services import my_job
        sleep(2)
        my_job()
