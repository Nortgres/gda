from flights.models import Security
from rest_framework import serializers


class SecuritySerializer(serializers.ModelSerializer):


    class Meta:
        model = Security
        fields = ('__all__')