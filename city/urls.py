from django.urls import path
from requests.api import get

from .views import index, get_city_weather

urlpatterns = [
    path('', index, name='index'),
    path('<str:city>/', get_city_weather, name='city_weather')
]
