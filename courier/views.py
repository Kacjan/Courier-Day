from django.shortcuts import render, redirect

from django.views import View
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CourierDayModelForm
from .models import CourierDay
# class CourierDayListView(ListView):
#     template_name = 'courier_day_list_view.html'
#     model = CourierDay


class Home(TemplateView):
    template_name = 'home.html'

#         )
class CourierDayCreateView(LoginRequiredMixin, CreateView):


    template_name = 'create_day.html'
    form_class = CourierDayModelForm
    success_url = reverse_lazy('courier_day_list_view')



class CourierDayListView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request,
            template_name='courier_day_list_view.html',
            # context={'days': CourierDay.objects.all() }
            context={'days': CourierDay.objects.filter(user_id=request.user)}
        )

class UpdateCourierDay(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = CourierDay
    form_class = CourierDayModelForm
    success_url = reverse_lazy('courier_day_list_view')

class DeleteCourierDay(LoginRequiredMixin, DeleteView):
    template_name = 'confirm_day_delete.html'
    model = CourierDay
    success_url = reverse_lazy('courier_day_list_view')






