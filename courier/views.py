from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CourierDayModelForm
from .models import CourierDay
#
class Home(TemplateView):
    template_name = 'home.html'

# Klasa wyświetlająca listę dni kurierskich
class CourierDayView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request,
            template_name='courier_day_view.html',
            # filtruje wyświetlanie listy dni przez danego użytkownika
            context={'days': CourierDay.objects.filter(user_id=request.user)}
        )

# Klasa CreateView odpowiedzialna za Formularz dodający dzień
class CourierDayCreateView(LoginRequiredMixin, CreateView):


    template_name = 'create_day.html'
    form_class = CourierDayModelForm
    success_url = reverse_lazy('courier_day_view')

# Wyświetla formularz do zmiany danych dnia w bazie danych
class UpdateCourierDay(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = CourierDay
    form_class = CourierDayModelForm
    success_url = reverse_lazy('courier_day_view')


# Usuwa dzień z bazy danych
class DeleteCourierDay(LoginRequiredMixin, DeleteView):
    template_name = 'confirm_day_delete.html'
    model = CourierDay
    success_url = reverse_lazy('courier_day_view')






