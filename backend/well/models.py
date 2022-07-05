from django.db import models

# Create your models here.

class Ohio(models.Model):
    api_well_number=models.CharField(max_length=15)
    quater=models.CharField(max_length=2)
    oil=models.FloatField(default=0)
    gas=models.FloatField(default=0)
    brine=models.FloatField(default=0)
    
    def __str__(self):
        return self.api_well_number