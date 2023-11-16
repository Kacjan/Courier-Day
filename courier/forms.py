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

    # Ogranicza wybór pola 'packages' do obiektów Facility przypisanego do użytkownika
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)


        if user.profile.facility:
            self.fields['packages'].queryset = user.profile.facility.facilitypackages_set.all()

        else:
            # Jeśli użytkownik nie ma przypisanego obiektu Facility, wyłącza wybór dnia
            self.fields['packages'].widget.attrs['disabled'] = True
            self.fields['packages'].help_text = 'Przypisz swoje konto do Oddziału, aby móc wybrać Datę.'



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
