from rest_framework import serializers
from .models import Vegetable ,Fruit

class VegetableSerializer(serializers.ModelSerializer):
     class Meta:
        model = Vegetable
        fields ='__all__'


class FruitSerializer(serializers.ModelSerializer):
     class Meta:
        model = Fruit
        fields ='__all__'





