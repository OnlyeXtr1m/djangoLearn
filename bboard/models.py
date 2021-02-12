from django.db import models


class Rubric(models.Model):
    rubric_name = models.CharField(max_length=20, null=True, verbose_name="Название")

    def __str__(self):
        return self.rubric_name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["rubric_name"]


class Bb(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    was_published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    rubric = models.ForeignKey("Rubric", on_delete=models.PROTECT, null=True, verbose_name="Категория")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["-was_published"]
