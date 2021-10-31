import json
from django.conf.urls import url
from django.http.response import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path("v1/cities", views.CityList.as_view()),
    path("v1/cities/<int:pk>", views.CityDetails.as_view()),
    path("v1/flights", views.FlightList.as_view()),
    path("v1/flights/<int:pk>", views.FlightDetails.as_view()),
]