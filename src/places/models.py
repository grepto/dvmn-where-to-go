from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', max_length=200)
    description_long = models.TextField('Подробное описание')
    longitude = models.FloatField('Широта')
    latitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    verbose_name = 'Фотография'
    verbose_name_plural = 'Фотографии'
    image = models.ImageField('Картинка')
    sort_order = models.IntegerField('Позиция')
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.sort_order} {self.place}'
