from django.db import models
from django.contrib.auth.models import User


class Bb(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Товар'
    )
    content = models.TextField(
        max_length=200,
        verbose_name='Описание'
    )
    prise = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Цена'
    )
    published = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Опубликовано'
    )
    rubric = models.ForeignKey(
        'Rubric',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Рубрика',
        related_name='entries'
    )

    class Kinds(models.TextChoices):
        BYU = 'b', 'куплю'
        SELL = 's', 'продам'
        EXCHANGE = 'c', 'Обменяю'
        RENT = 'r'  # последний элементы будет выводиться как RENT
        __empty__ = 'Выберите тип публикуемого объявления'

    kind = models.CharField(max_length=1,
                            choices=Kinds.choices,
                            default=Kinds.SELL)

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published', 'title']
        unique_together = (
            ('published', 'title'),
            ('title', 'prise', 'rubric'),
        ) # создадим запрет на спам одинаковых объявлений
        get_latest_by = 'published' # метод latest вернет последнюю публикацию


class Rubric(models.Model):
    name = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
