# Generated by Django 4.2.2 on 2024-06-16 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailing_interface_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="clientservice",
            options={"verbose_name": "клиент", "verbose_name_plural": "клиенты"},
        ),
    ]
