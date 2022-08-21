from django.shortcuts import render
import requests
from .forms import CityWeatherForm
from django.http import JsonResponse
from django.conf import settings

def index(request):
    api_key = settings.WEATHER_API_KEY
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    city = 'Las Vegas'
    form = CityWeatherForm()

    weather = {}
    if request.method == 'POST':
        form = CityWeatherForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            city = cd['city_name']
            city_weather = requests.get(url.format(city, api_key)).json()
            
            weather = {
                    'city' : city,
                    'temperature' : city_weather['main']['temp'],
                    'description' : city_weather['weather'][0]['description'],
                    'icon' : city_weather['weather'][0]['icon']
                }
        #     return JsonResponse({'success': True})
        # else:
        #     return JsonResponse({'success': False, 'errors': form.errors})

    context = {'weather': weather, 'form': form}
    return render(request, 'index.html', context)
