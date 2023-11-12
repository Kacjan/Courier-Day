from django.forms import ModelForm

from django import forms
from .models import CourierDay
from django.contrib.auth import get_user_model
User = get_user_model()


class CourierDayModelForm(ModelForm):

    # wyświetla pola modelu CourierDay poza userem - on jest uzupełniany automatycznie przez walidację w widoku
    class Meta:
        model = CourierDay
        exclude = ['user']

# formularz do filtrowania dni na podstawie daty
class DateFilterForm(forms.Form):
    # required=False oznacza ze wypełnianie pól jest opcjonalne,
    start_date = forms.DateField(required=False,
                                 widget=forms.DateInput(attrs={'type': 'date'}),
                                 label='Dzień początkowy'
                                 )
    end_date = forms.DateField(required=False,
                               widget=forms.DateInput(attrs={'type': 'date'}),
                               label='Dzień końcowy'
                               )
