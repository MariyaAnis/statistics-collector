from django.db import models


class City(models.Model):
    name = models.CharField('название', max_length=200)
    lat = models.SmallIntegerField('широта')
    lon = models.SmallIntegerField('долгота')
    country = models.CharField('страна', max_length=200)

    class Meta:
        unique_together = ('lat', 'lon')
