from django.http import HttpResponse
import json
from rest_framework import generics
from api.serializers import PersonSerializer
from api.models import Person

def index(request):
    welcome_message = {'message': 'Welcome to API /v1!'}
    return HttpResponse(json.dumps(welcome_message, indent=4, sort_keys=True), content_type="application/json")

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
