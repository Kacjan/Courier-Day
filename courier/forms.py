from django.forms import ModelForm, Form, CharField, IntegerField, TimeField

from django import forms
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



# class CourierDayForm(Form):
#     user = CharField(min_length=1, max_length=30, widget=forms.Select(attrs={'disabled':True}))
#     packages = IntegerField(min_value=1, max_value=6)
#     addresses = IntegerField(min_value=1, max_value=3)
#     machine = IntegerField(min_value=1, max_value=3)
#     stops_end = TimeField()
#     pickup_end = TimeField()
#
#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('request').user
#         super(CourierDayForm, self).__init__(*args, **kwargs)
#         self.fields['user'].initial=self.user
#
#     def clean_packages(self,*args, **kwargs):
#         packages = self.cleaned_data.get('packages')
#         if str in packages:
#             raise forms.ValidationError('This is not a valid input')
#         else:
#             return packages
#
#     def clean_addresses(self,*args, **kwargs):
#         addresses = self.cleaned_data.get('addresses')
#         if str in addresses:
#             raise forms.ValidationError('This is not a valid input')
#         else:
#             return addresses


    # def clean(self):
    #     result = super().clean()
    #     if result