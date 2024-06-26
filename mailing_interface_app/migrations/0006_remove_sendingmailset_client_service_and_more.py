# Generated by Django 4.2.2 on 2024-06-17 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing_interface_app", "0005_alter_sendingmailset_message_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sendingmailset",
            name="client_service",
        ),
        migrations.AddField(
            model_name="sendingmailset",
            name="client_service",
            field=models.ManyToManyField(
                related_name="client", to="mailing_interface_app.clientservice"
            ),
        ),
    ]
