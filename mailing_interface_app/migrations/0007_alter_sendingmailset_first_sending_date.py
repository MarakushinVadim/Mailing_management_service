# Generated by Django 4.2.2 on 2024-06-18 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing_interface_app", "0006_remove_sendingmailset_client_service_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sendingmailset",
            name="first_sending_date",
            field=models.DateTimeField(verbose_name="дата первой отправки"),
        ),
    ]
