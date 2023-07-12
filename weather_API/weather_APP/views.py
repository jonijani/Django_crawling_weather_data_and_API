

from django.shortcuts import render
import json
from django.http import JsonResponse
from crawling.main import get_weather_for_city_searched


#  http://127.0.0.1:8000/weather_api/london/
def get_weather_news(request,city):
    data = get_weather_for_city_searched(city)
    json_data = JsonResponse(data,safe=False)
    return json_data











