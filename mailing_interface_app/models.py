from django.db import models
from pytils.translit import slugify

from users_app.models import User

NULLABLE = {"blank": True, "null": True}


class ClientService(models.Model):
    email = models.EmailField(unique=True, verbose_name="email")
    name = models.CharField(
        max_length=100, verbose_name="Ф.И.О.", help_text="Введите Ф.И.О."
    )
    comment = models.TextField(
        max_length=255,
        verbose_name="комментарий",
        help_text="Введите комментарий",
        **NULLABLE,
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="укажите владельца рассылки",
        **NULLABLE,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.name}, {self.email}"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Message(models.Model):
    letter_subject = models.CharField(max_length=255, verbose_name="тема письма")
    slug = models.SlugField(
        max_length=255, unique=True, verbose_name="ссылка", **NULLABLE
    )
    letter_body = models.TextField(verbose_name="тело письма")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="пользователь", **NULLABLE
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.letter_subject)
        super(Message, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"

    def __str__(self):
        return f"{self.letter_subject}, {self.user}"


class SendingMailSet(models.Model):
    class SendingPeriodChoices(models.TextChoices):
        ONE_IN_MONTH = "one_in_month", "один раз в месяц"
        ONE_IN_WEEK = "one_in_week", "один раз в неделю"
        ONE_IN_DAY = "one_in_day", "один раз в день"

    class SendingStatusChoices(models.TextChoices):
        COMPLETED = "completed", "завершена"
        CREATED = "created", "создана"
        RUNNING = "running", "выполняется"

    name = models.CharField(
        max_length=255, verbose_name="имя рассылки", help_text="Введите имя рассылки"
    )
    client_service = models.ManyToManyField(ClientService, related_name="client")
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, verbose_name="сообщение"
    )
    first_sending_date = models.DateTimeField(
        verbose_name="дата первой отправки",
        help_text="Введите дату и время отправки в формате ДД.ММ.ГГГГ 00:00:00",
    )
    next_sending_time = models.DateTimeField(
        verbose_name="дата и время следующей отправки", **NULLABLE
    )
    sending_period = models.CharField(
        max_length=13,
        default=SendingPeriodChoices.ONE_IN_WEEK,
        choices=SendingPeriodChoices.choices,
        verbose_name="период отправки",
    )
    sending_status = models.CharField(
        max_length=9,
        default=SendingStatusChoices.CREATED,
        choices=SendingStatusChoices.choices,
        verbose_name="статус отправки",
    )
    is_active = models.BooleanField(
        default=True, verbose_name="состояние активности рассылки"
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="укажите владельца рассылки",
        **NULLABLE,
        on_delete=models.SET_NULL,
    )

    def save(self, *args, **kwargs):
        if self.next_sending_time is None:
            self.next_sending_time = self.first_sending_date
        super(SendingMailSet, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"
        permissions = (
            ("can_view_sending_mail_set", "Can view sending mail set"),
            ("can_edit_is_active", "Can edit active sending mail set"),
        )

    def __str__(self):
        return f"Имя рассылки - {self.name}"


class SendTry(models.Model):
    class StatusChoices(models.TextChoices):
        SUCCESS = "SUCCESS", "успешно"
        FAILURE = "FAILURE", "неудачно"

    sending_mail = models.ForeignKey(
        SendingMailSet, on_delete=models.CASCADE, verbose_name="отправка"
    )
    status = models.CharField(
        max_length=7,
        default=StatusChoices.FAILURE,
        choices=StatusChoices.choices,
        verbose_name="статус попытки отправки",
    )
    last_sending_date = models.DateTimeField(
        auto_now_add=True, verbose_name="дата последней попытки отправки"
    )
    server_response = models.TextField(
        verbose_name="ответ почтового сервера", **NULLABLE
    )

    class Meta:
        verbose_name = "попытка отправки"
        verbose_name_plural = "попытки отправки"

    def __str__(self):
        return f"Попытка отправки - {self.sending_mail}"
