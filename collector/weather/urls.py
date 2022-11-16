from django.urls import path

from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.save_weather, name='save_weather'),

]
