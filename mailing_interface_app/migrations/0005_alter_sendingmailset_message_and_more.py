# Generated by Django 4.2.2 on 2024-06-16 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mailing_interface_app", "0004_alter_sendingmailset_sending_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sendingmailset",
            name="message",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="mailing_interface_app.message",
                verbose_name="сообщение",
            ),
        ),
        migrations.AlterField(
            model_name="sendingmailset",
            name="sending_time",
            field=models.TimeField(
                help_text="Введите время отправки в формате 00:00:00",
                verbose_name="время отправки",
            ),
        ),
    ]
