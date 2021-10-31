from django.http import HttpResponse
import json
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import CitySerializer, FlightSerializer
from api.models import City, Flight

def index(request):
    welcome_message = {'message': 'Welcome to API /v1!'}
    return HttpResponse(json.dumps(welcome_message, indent=4, sort_keys=True), content_type="application/json")

class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all().order_by('cityId')
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'country']

class CityDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class FlightList(generics.ListCreateAPIView):
    queryset = Flight.objects.all().order_by('flightId')
    serializer_class = FlightSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'flight_from', 'flight_to']

class FlightDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
