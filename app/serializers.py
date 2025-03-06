from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Weather

class Weather_infoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]



