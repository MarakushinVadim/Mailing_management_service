# Generated by Django 4.2.2 on 2024-06-21 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mailing_interface_app", "0013_sendingmailset_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="clientservice",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="укажите владельца рассылки",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
    ]
