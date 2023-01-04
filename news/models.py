from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(
        max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Создан')
    created_at = models.DateTimeField(
        auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/', verbose_name='Фото', default='ava.jpg')
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT,
        verbose_name='Категория')

    def my_func(self):
        return "Hello world"

    # def get_absolute_url(self):
        # return reverse("view_news", kwargs={"news_id": self.pk})

    def get_absolute_url(self):
        return reverse("view_news", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(
        max_length=150, verbose_name='Наименование категории', db_index=True)

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['-title']
