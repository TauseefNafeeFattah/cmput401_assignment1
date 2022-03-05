from rest_framework import serializers
from . models import CoffeeRoaster

class CoffeeRoasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeRoaster
        fields = ['id','name','farm','region','fermentation','price']
class CoffeeRoasterViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeRoaster
        fields = ['id','name','price']
