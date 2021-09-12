from django.contrib import admin
from . models import OpenWeatherCity
# Register your models here.

@admin.register(OpenWeatherCity)
class OpenWeatherCityAdmin(admin.ModelAdmin):
    list_display = ['id', 'open_weather_id', 'name', 'country']