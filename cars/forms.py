from django import forms
from cars.models import Brand

class CarForm(forms.Form):
    model = forms.CharField()
    brand = forms.ModelChoiceField(Brand.objects.all())
    version = forms.CharField()
    motor = forms.CharField()
    category = forms.CharField()
    transmission = forms.CharField()
    fuel_type = forms.CharField()
    color = forms.CharField()
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    price = forms.FloatField()
    state = forms.CharField()
    photo = forms.ImageField()