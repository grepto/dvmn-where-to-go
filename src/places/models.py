from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    """The model for the place"""
    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Краткое описание', max_length=300, blank=True)
    long_description = HTMLField('Подробное описание', blank=True)
    longitude = models.FloatField('Широта', blank=True, default=0)
    latitude = models.FloatField('Долгота', blank=True, default=0)

    def __str__(self):
        return str(self.title)


class PlaceImage(models.Model):
    """The model for photo for the place"""

    image = models.ImageField('Фотография')
    sort_order = models.PositiveIntegerField('Позиция', default=0)
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images', verbose_name='Место')

    class Meta:
        ordering = ['sort_order']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.sort_order} {self.place}'
