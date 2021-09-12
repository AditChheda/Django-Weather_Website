from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'weather_visualization_app/index.html')