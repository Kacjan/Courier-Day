from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CourierDayModelForm, DateFilterForm
from .models import CourierDay


class Home(TemplateView):
    template_name = 'home.html'


# Klasa wyświetlająca listę dni kurierskich
class CourierDayView(LoginRequiredMixin, View):

    def get(self, request):
        form = DateFilterForm(request.GET)
        # filtruje wyświetlanie listy dni przez zalogowanego usera
        days = CourierDay.objects.filter(user_id=request.user)
        # days = CourierDay.objects.filter(user=request.user)

        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')

            if start_date:
                # filtruje dzień do większych lub równych od daty startowej
                days = days.filter(packages__date__gte=start_date)
            if end_date:
                # filtruje dzień do mniejszych lub równych do daty końcowej
                days = days.filter(packages__date__lte=end_date)

        return render(
            request,
            template_name='courier_day_view.html',
            # przekazuje filtrowanie przez usera, oraz formularz
            context={'days': days, 'form': form}
        )


# Klasa CreateView odpowiedzialna za Formularz dodający dzień
class CourierDayCreateView(LoginRequiredMixin, CreateView):

    template_name = 'create_day.html'
    form_class = CourierDayModelForm
    success_url = reverse_lazy('courier_day_view')

    # Dodaje i zwraca obiekt użytkowinia do obiektów formularza
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    # Uzupełnia niewidoczne w formularzu pole user zalogowanym userem
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Wyświetla formularz do zmiany danych dnia w bazie danych
class UpdateCourierDay(LoginRequiredMixin, UpdateView):
    template_name = 'edit_day.html'
    model = CourierDay
    form_class = CourierDayModelForm
    success_url = reverse_lazy('courier_day_view')


# Usuwa dzień z bazy danych
class DeleteCourierDay(LoginRequiredMixin, DeleteView):
    template_name = 'confirm_day_delete.html'
    model = CourierDay
    success_url = reverse_lazy('courier_day_view')

