from django.db import models
from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from django.dispatch import receiver


User = get_user_model()

"""Jak dodać foreign key"""
"""Czy muszę określać min/max przy IntegerField w modelu"""

"""W CourierDay w polu packages mam połączenie do tabeli FacilityPackages.
Teraz przez ten klucz moge dostać się do wszystkich pól FacilityPackages np CourierDay.packages.date
CourierDay.packages.packages
"""


class CourierDay(models.Model):

    user = models.ForeignKey(User, models.SET_NULL, null=True)
    packages = models.ForeignKey('FacilityPackages', models.SET_NULL, null=True)
    addresses = models.IntegerField()
    machine = models.IntegerField()
    stops_end = models.TimeField()
    pickup_end = models.TimeField()

    added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.packages.date}'

class FacilityPackages(models.Model):
    date = models.DateField()
    packages = models.IntegerField()
    facility = models.ForeignKey('Facility', models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.date}'

class Facility(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name