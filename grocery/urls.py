from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [

    path('vegetables/', views.VegetableList.as_view(),
    name='vegetable_list'),

    path('vegetables/<int:pk>', views.VegetableDetail.as_view(), 
    name='vegetable_detail'),


    path('fruits/', views.FruitList.as_view(),
    name='fruit_list'),
    
    path('fruits/<int:pk>', views.FruitDetail.as_view(), 
    name='fruit_detail'),
]