from django.contrib import admin
from django.urls import path, include
from calories.views import (
    predict_calories,
    home
)


urlpatterns = [
    path('', home, name="home"),
    path('predict/', predict_calories, name="predict_calories")
]
