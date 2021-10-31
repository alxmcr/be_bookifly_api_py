from django.db import models

class City(models.Model):
    cityId = models.BigAutoField(primary_key=True)
    name = models.CharField("Name", max_length=50, unique=True, null=False)
    country = models.CharField("Country", max_length=50, null=False)

    def __str__(self):
        return f"{self.name} {self.country}"

class Flight(models.Model):
    flightId = models.BigAutoField(primary_key=True)
    date = models.DateField("Date", null=False)
    departure = models.TimeField("Departure", null=False)
    arrival = models.TimeField("Arrival", null=False)
    duration = models.TimeField("Duration", null=False)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2, null=False)
    flight_from = models.ForeignKey(City, on_delete=models.CASCADE, null=False, related_name="flight_from")
    flight_to = models.ForeignKey(City, on_delete=models.CASCADE, null=False, related_name="flight_to")

    def __str__(self):
        return f"{self.flight} {self.date} {self.flight_from} {self.flight_to}"
