from rest_framework import serializers
from .models import Person

class PersonDetailSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'phone')

class PhoneNumSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'phone')
