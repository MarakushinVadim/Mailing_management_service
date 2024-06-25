from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="почта", unique=True)
    is_active = models.BooleanField(
        default=True, verbose_name="состояние активности пользователя"
    )
    token = models.CharField(max_length=255, verbose_name="Token", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = (
            ("can_view_users", "Can view users"),
            ("can_edit_is_active", "Can edit active users"),
        )
