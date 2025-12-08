from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    
    
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    version = models.CharField(max_length=150)
    motor = models.CharField(max_length=15, null=True)
    category = models.CharField(max_length=150, null=True)
    transmission = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    price = models.FloatField(blank=True, null=True)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.model
        