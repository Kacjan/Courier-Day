from django.forms import ModelForm, Form, CharField
from .models import CourierDay
from django.contrib.auth import get_user_model
User = get_user_model()
'''Dodać Courier Id musi byc w bazie danych

courier_id = forms.IntegerField(Must be registered)
coś w tym stylu?

Albo lepiej! Powinno ładować id zalogowanego użytkownika!
'''

class CourierDayModelForm(ModelForm):

    class Meta:
        model = CourierDay
        fields = '__all__'
        """walidacja na frontendzie"""
        widgets={
            'user': forms.Select(attrs={'disabled':True})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('request').user
        super(CourierDayModelForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial=self.user



class CpurierDayForm(Form):
    user = CharField()
    packages
    addresses
    machine
    stops_end
    pickup_end

