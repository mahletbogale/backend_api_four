from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import VegetableSerializer ,FruitSerializer 
from .models import Vegetable,Fruit

class VegetableList(generics.ListCreateAPIView):
    queryset = Vegetable.objects.all()
    serializer_class =  VegetableSerializer 

class VegetableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vegetable.objects.all()
    serializer_class = VegetableSerializer


class FruitList(generics.ListCreateAPIView):
    queryset = Fruit.objects.all()
    serializer_class =  FruitSerializer 

class FruitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer




