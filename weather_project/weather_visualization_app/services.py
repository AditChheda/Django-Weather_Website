import requests
from django.conf import settings

def weather_data_for_city(city_id):
    api_url = settings.OPEN_WEATHER_BASE_URL + f"weather?id={city_id}&appid={settings.OPEN_WEATHER_API_KEY}&units=metric"
    resp = requests.get(api_url)
    return resp.json()