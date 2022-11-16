from django.db import models


class City(models.Model):
    name = models.CharField('название', max_length=200)
    country = models.CharField('страна', max_length=200)
    lat = models.FloatField('широта')
    lon = models.FloatField('долгота')

    class Meta:
        unique_together = ('lat', 'lon')
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}, {self.country}'
