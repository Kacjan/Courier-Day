from django.db import models
from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from django.dispatch import receiver


User = get_user_model()

"""W CourierDay w polu packages mam połączenie do tabeli FacilityPackages.
Teraz przez ten klucz moge dostać się do wszystkich pól FacilityPackages np CourierDay.packages.date
CourierDay.packages.packages
"""


class CourierDay(models.Model):

    user = models.ForeignKey(User, models.SET_NULL, null=True)
    packages = models.ForeignKey('FacilityPackages', models.SET_NULL, null=True, verbose_name="Data")
    addresses = models.IntegerField(verbose_name="adresy")
    machine = models.IntegerField(verbose_name="paczkomat")
    stops_end = models.TimeField(verbose_name="konec adresów")
    pickup_end = models.TimeField(verbose_name="koniec zbiorów")

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