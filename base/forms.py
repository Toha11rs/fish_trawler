from django import forms
from django.forms import DateInput
from fish import models

class NavigationForm(forms.ModelForm):
    class Meta:
        model = models.navigation
        fields = ['catch', 'date_navigation', 'capitan', 'trawler']
        widgets = {
            'date_navigation': forms.DateInput(attrs={'type': 'date'}),
        }

class TrawlerForm(forms.ModelForm):
    class Meta:
        model = models.trawler
        fields = ['name','spaciousness']