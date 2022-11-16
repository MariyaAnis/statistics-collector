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
    clouds = models.SmallIntegerField('облачность', blank=True, null=True)
    wind_speed = models.SmallIntegerField('скорость ветра', blank=True, null=True)
    rain = models.SmallIntegerField('количество осадков (дождя)', blank=True, null=True)
