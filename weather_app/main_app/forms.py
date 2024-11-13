from django import forms

class TownForm(forms.Form):
    town_name = forms.CharField(label='Town Name', max_length=100)
