from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    """The model for the place"""
    title = models.CharField('Название', max_length=200, null=False, blank=False)
    description_short = models.TextField('Краткое описание', max_length=300, null=False, blank=True, default='')
    description_long = HTMLField('Подробное описание', null=False, blank=True, default='')
    longitude = models.FloatField('Широта', null=False, blank=True, default=0)
    latitude = models.FloatField('Долгота', null=False, blank=True, default=0)

    def __str__(self):
        return str(self.title)


class PlaceImage(models.Model):
    """The model for photo for the place"""
    verbose_name = 'Фотография'
    verbose_name_plural = 'Фотографии'
    image = models.ImageField('Картинка')
    sort_order = models.PositiveIntegerField('Позиция', default=0, blank=False, null=False)
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images')

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return f'{self.sort_order} {self.place}'
