from django.db import models

from users_app.models import User

NULLABLE = {"blank": True, "null": True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок', help_text='Введите заголовок')
    body = models.TextField(verbose_name="Содержимое", help_text="Введите содержимое")
    avatar = models.ImageField(upload_to="media", **NULLABLE, verbose_name="Превью")
    count_view = models.IntegerField(default=0)
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации", **NULLABLE)
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        help_text='укажите владельца рассылки',
        **NULLABLE,
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

    def __str__(self):
        return f'Название блога- {self.title}'
