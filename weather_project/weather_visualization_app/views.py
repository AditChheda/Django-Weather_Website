from django.shortcuts import render, redirect
from . services import weather_data_for_city
from . models import OpenWeatherCity

# Create your views here.

def home_page(request):
    city_data = OpenWeatherCity.objects.all()
    if request.method == "POST":
        pk = request.POST['select_city']
        if pk:
            weather_data = weather_data_for_city(city_id = pk)
            context = {
                'weather_data': weather_data,
                'city_data': city_data,
            }
            return render(request, 'weather_visualization_app/index.html', context)
        else:
            return redirect('/')
    else:
        # weather_data = weather_data_for_city(city_id = 232307)
        # weather_data = {
        #     'coord': {'lon': 31.8811, 'lat': 0.1772}, 
        #     'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 
        #     'base': 'stations', 'main': {'temp': 294.16, 'feels_like': 293.88, 'temp_min': 294.16, 
        #     'temp_max': 294.16, 'pressure': 1015, 'humidity': 60, 'sea_level': 1015, 'grnd_level': 880}, 
        #     'visibility': 10000, 'wind': {'speed': 0.5, 'deg': 43, 'gust': 1.04}, 'clouds': {'all': 99}, 
        #     'dt': 1631513196, 'sys': {'country': 'UG', 'sunrise': 1631504711, 'sunset': 1631548316}, 
        #     'timezone': 10800, 'id': 232307, 'name': 'Kanoni', 'cod': 200
        # }

        # city_data = OpenWeatherCity.objects.all()

        # context = {
        #     'weather_data': weather_data,
        #     'city_data': city_data,
        # }
        return render(request, 'weather_visualization_app/index.html', {'city_data': city_data})