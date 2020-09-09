from django.db import models

# Create your models here.

class Vegetable(models.Model):
        name = models.CharField(max_length=100)
        price= models.DecimalField(max_digits=6, decimal_places=2) 
        lebel=models.CharField(max_length=100)
        description = models.TextField()
        count = models.IntegerField(default=0) 
        image_url = models.TextField()


        def __unicode__(self):
            return self.name

class Fruit(models.Model):
        name = models.CharField(max_length=100)
        price= models.DecimalField(max_digits=6, decimal_places=2) 
        lebel=models.CharField(max_length=100)
        description = models.TextField()
        count = models.IntegerField(default=0) 
        image_url = models.TextField()


        def __unicode__(self):
             return self.name



