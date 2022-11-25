from rest_framework import serializers
from .models import User,Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['username','password','email']


class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields= ['name','age','height','weight','prevcondition','medication','location']


