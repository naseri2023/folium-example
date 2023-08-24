from django.db import models


# Create your models here.
class EVChargingLocation(models.Model):
    Station_Name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.Station_Name
