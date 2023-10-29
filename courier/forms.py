from django.forms import ModelForm

from django import forms
from .models import CourierDay
from django.contrib.auth import get_user_model
User = get_user_model()

class CourierDayModelForm(ModelForm):

    class Meta:
        model = CourierDay
        exclude = ['user']
        # widgets={
        #     'user': forms.Select(attrs={'disabled':True})
        # }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CourierDayModelForm, self).__init__(*args, **kwargs)
        # self.fields['user'].initial=self.user