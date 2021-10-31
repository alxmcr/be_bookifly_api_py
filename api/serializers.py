from api.models import City, Flight
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            "cityId",
            "name",
            "country"
        ]

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            "flightId",
            "date",
            "departure",
            "arrival",
            "duration",
            "price",
            "flight_from",
            "flight_to"
        ]