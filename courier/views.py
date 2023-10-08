from django.shortcuts import render
from .models import CourierDay
from django.views.generic import ListView

class CourierDayListView(ListView):
    template_name = 'courier_day_list_view.html'
    model = CourierDay