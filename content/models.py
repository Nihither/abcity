from datetime import datetime
from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание")
    video = models.FileField(upload_to='video', verbose_name="Видео")
    thumbnail = models.FileField(upload_to='thumbnails', verbose_name="Постер")
    created = models.DateTimeField(verbose_name="Создано", default=datetime.now)

    def __str__(self):
        return self.name
