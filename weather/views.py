from django.shortcuts import render
import requests
from .forms import ForecastForm
from datetime import datetime
from math import ceil
import os

def get_Data(city_name):
    api_key = os.environ.get('api_key')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    try:

        response = requests.get(url).json()

        if response['cod'] == 200:
            return response
        else:
            return "Houve um erro ao carregar os dados"
    
    except (requests.ConnectionError, requests.ConnectTimeout, requests.HTTPError):
        return f"Erro: Erro ao obter dados da API"

def weather(request):

    form = ForecastForm()
    city_name = 'Lisboa'
    forecast = get_Data(city_name)

    if request.method == 'POST':

        form = ForecastForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city']  
            forecast = get_Data(city_name)
            icon = forecast['weather'][0]['icon']
    
    icon = f"https://openweathermap.org/img/wn/{forecast['weather'][0]['icon']}@2x.png"
    filter_data = {'temperature': ceil(forecast['main']['temp'] - 273.15),'hour':datetime.now().strftime("%H:%M"),'icon':icon,'city':forecast['name']}


    return render(request, "index.html",{'form':form,'forecast': filter_data})

