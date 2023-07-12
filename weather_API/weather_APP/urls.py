from django.contrib import admin
from django.urls import path ,include
from weather_APP.views import get_weather_news



urlpatterns = [
   path('<str:city>/', get_weather_news, name='get_weather_news')
    
]