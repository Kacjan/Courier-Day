from django.forms import ModelForm

from django import forms
from .models import CourierDay
from django.contrib.auth import get_user_model
User = get_user_model()

class CourierDayModelForm(ModelForm):

    class Meta:
        model = CourierDay
        exclude = ['user']
