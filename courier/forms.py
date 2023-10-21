from django import forms
from .models import CourierDay

'''Dodać Courier Id musi byc w bazie danych

courier_id = forms.IntegerField(Must be registered)
coś w tym stylu?

Albo lepiej! Powinno ładować id zalogowanego użytkownika!
'''

class CourierDayModelForm(forms.ModelForm):
    class Meta:
        model = CourierDay
        fields = '__all__'

