from django.db import models

from cities.models import City


class Weather(models.Model):
    city = models.ForeignKey(
        City,
        verbose_name='город',
        on_delete=models.CASCADE,
        related_name='weather_now'
    )
    temp = models.SmallIntegerField('температура')

    class Meta:
        verbose_name = 'Погода'
        verbose_name_plural = 'Погода'

    def __str__(self):
        return f'{self.city.name}: {self.temp}'
