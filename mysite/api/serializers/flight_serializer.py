from flights.models import Flight
from rest_framework import serializers
from .airport_serializer import AirportSerializer

class FlightSerializer(serializers.ModelSerializer):
    origin = AirportSerializer()# many=True в случае если связь ManyToMany
    destination = AirportSerializer()

    class Meta:
        model = Flight
        fields = ('__all__')
