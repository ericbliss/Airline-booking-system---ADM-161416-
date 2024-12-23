from django.shortcuts import render
from rest_framework import viewsets
from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer

# Create your views here.

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
