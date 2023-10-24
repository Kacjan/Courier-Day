from django.contrib import admin
from .models import CourierDay, FacilityPackages, Facility

admin.site.register(CourierDay)
admin.site.register(FacilityPackages)
admin.site.register(Facility)
# admin.site.register(Profile)