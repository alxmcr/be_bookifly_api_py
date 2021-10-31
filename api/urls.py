import json
from django.conf.urls import url
from django.http.response import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path("v1/people", views.PersonList.as_view())
]