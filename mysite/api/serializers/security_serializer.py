from flights.models import Security
from rest_framework import serializers
from .user_serializer import UserSerializer
from string import punctuation


class SecuritySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def validate_name(self, value):
        baned_symbols = set(punctuation)
        baned_symbols.extend(['0','1','2','3','4','5','6','7','8','9'])
        for i in value:
            for i in baned_symbols:
                    raise serializers.ValidationError('Могут содержаться только буквы')
        return value

    def validate_second_name(self, value):
        alphabet = 'йцукенгшщзхъфывапролджэячсмитьбю'
        for i in value:
            if i not in alphabet:
                    raise serializers.ValidationError('Могут содержаться только буквы')
        return value
    class Meta:
        model = Security
        fields = ('__all__')