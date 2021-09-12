from django.core.management.base import BaseCommand, CommandError
from weather_visualization_app.models import OpenWeatherCity
import json

# python manage.py load_city_data

class Command(BaseCommand):
    help = "Load open weather city data from JSON file."

    def handle(self, *args, **kwargs):
        with open("weather_visualization_app/data/city.list.json", "r", encoding="utf8") as f:
            city_list = json.loads(f.read())

        for city in city_list:
            ow_city_id = city['id']
            OpenWeatherCity.objects.update_or_create(
                open_weather_id = ow_city_id,
                defaults = {
                    "name": city['name'],
                    "country": city['country'],
                }
            )

        self.stdout.write(self.style.SUCCESS("Successfully Loaded Data from JSON file."))