import requests
from django.shortcuts import render

from .forms import TownForm


def index(request):
    weather_data = None  # Initialize weather data variable

    if request.method == 'POST':
        form = TownForm(request.POST)
        if form.is_valid():
            town_name = form.cleaned_data['town_name']

            # Replace 'your_api_key' with your actual API key
            api_key = '826b97ae066d39e279901e86a67f6419'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={town_name}&appid={api_key}&units=metric'

            # Send request to the weather API
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {'error': 'City not found or API error'}

    else:
        form = TownForm()

    return render(request, 'index.html', {'form': form, 'weather_data': weather_data})
