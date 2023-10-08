from django.db import models


"""Jak dodać foreign key"""
"""Czy muszę określać min/max przy IntegerField w modelu"""

class CourierDay(models.Model):
    date = models.DateField()
    courier_id = models.IntegerField()
    packages = models.IntegerField()
    adresy = models.IntegerField()
    paczkomat = models.IntegerField()
    stops_end = models.TimeField()
    pickup_end = models.TimeField()

    added = models.DateTimeField(auto_now_add=True, null=True)

# class FacilityPackages(models.Model):
#     id = models.IntegerField()
#     date = models.DateField()
#     packages = models.IntegerField()
#     facility_id = models.IntegerField()
# #
# # class Profile(models.Model):
# #     id = models.IntegerField()
# #     user_id = models.IntegerField()
# #     facility_id = models.IntegerField()
# #
# # class Facility(models.Model):
# #     id = models.IntegerField()
# #     name = models.CharField(max_length=50)
