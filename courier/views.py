from django.shortcuts import render

from django.views import View
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import CourierDayModelForm
from .models import CourierDay
# class CourierDayListView(ListView):
#     template_name = 'courier_day_list_view.html'
#     model = CourierDay


class Home(TemplateView):
    template_name = 'home.html'

"""Klasa Home bez szablonu"""
# class Home(View):
#     def get(self, request):
#         return render(
#             request,
#             template_name='home.html'
#         )

class CourierDayCreateView(CreateView):

    template_name = 'form.html'
    form_class = CourierDayModelForm
    success_url = reverse_lazy('courier_day_list_view')

class CourierDayListView(View):
    def get(self, request):
        return render(
            request,
            template_name='courier_day_list_view.html',
            context={'days': CourierDay.objects.all() }
        )

class UpdateCourierDay(UpdateView):
    template_name = 'form.html'
    model = CourierDay
    form_class = CourierDayModelForm
    success_url = reverse_lazy('courier_day_list_view')
    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)




