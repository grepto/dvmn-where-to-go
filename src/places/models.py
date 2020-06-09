from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200, null=False, blank=False)
    description_short = models.TextField('Краткое описание', max_length=200, null=False, blank=False)
    description_long = HTMLField('Подробное описание', null=True, blank=True)
    longitude = models.FloatField('Широта')
    latitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    verbose_name = 'Фотография'
    verbose_name_plural = 'Фотографии'
    image = models.ImageField('Картинка')
    sort_order = models.PositiveIntegerField('Позиция', default=0, blank=False, null=False)
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images')

    class Meta(object):
        ordering = ['sort_order']

    def __str__(self):
        return f'{self.sort_order} {self.place}'
