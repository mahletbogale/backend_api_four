from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Vegetable, Fruit 

# Register your models here.
admin.site.register(Vegetable)
admin.site.register(Fruit)
