from rest_framework import serializers
from .models import Flight, Passenger

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()

    class Meta:
        model = Passenger
        fields = '__all__'

    def validate(self, data):
        flight_data = data.get('flight')
        if not flight_data or not flight_data.get('id'):
            raise serializers.ValidationError("Flight ID is required.")
        return data

    def create(self, validated_data):
        flight_data = validated_data.pop('flight')
        flight_id = flight_data.get('id')
        flight = Flight.objects.get(id=flight_id)
        passenger = Passenger.objects.create(flight=flight, **validated_data)
        return passenger