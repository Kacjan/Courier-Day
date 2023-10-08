from django.db import models

class CourierDay(models.Model):
    date = models.DateField()
    courier_id = models.IntegerField()
    packages = models.IntegerField()
    adresy = models.IntegerField()
    paczkomat = models.IntegerField()
    stops_end = models.TimeField()
    pickup_end = models.TimeField()


# class Oddzial(models.Model):
#     oddzial_id = models.IntegerField()
#     date = models.DateField()
#     packages = models.IntegerField()

