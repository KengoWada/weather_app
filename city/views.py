from django.shortcuts import redirect, render

from .utils import get_weather

CITIES = {
    'kampala': {'lat': '0.3476', 'lon': '32.5825'},
    'nairobi': {'lat': '1.2921', 'lon': '36.8219'},
    'tokyo': {'lat': '35.6762', 'lon': '139.6503'},
    'london': {'lat': '51.5074', 'lon': '0.1278'},
    'paris': {'lat': '48.8566', 'lon': '2.3522'},
}


def index(request):
    weather_today = {}
    for key, value in CITIES.items():
        weather_today[key] = get_weather(value['lat'], value['lon'])
    context = {'weather': weather_today, 'cities': CITIES.keys()}
    return render(request, 'index.html', context=context)


def get_city_weather(request, city):
    if city not in CITIES.keys():
        return redirect('index')

    coordinates = CITIES[city]

    weather = get_weather(coordinates['lat'], coordinates['lon'])
    context = {'weather': weather, 'cities': CITIES.keys(), 'city': city}
    return render(request, 'city.html', context=context)
