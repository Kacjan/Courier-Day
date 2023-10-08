from django.shortcuts import render

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import CourierDayModelForm
from .models import CourierDay
class CourierDayListView(ListView):
    template_name = 'courier_day_list_view.html'
    model = CourierDay

class CourierDayCreateView(CreateView):

    template_name = 'form.html'
    form_class = CourierDayModelForm
    success_url = reverse_lazy('courier_day_list_view')

