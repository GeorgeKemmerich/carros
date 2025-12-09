from django import forms
from cars.models import Brand, Car

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

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            version = self.cleaned_data['version'],
            motor = self.cleaned_data['motor'],
            category = self.cleaned_data['category'],
            transmission = self.cleaned_data['transmission'],
            fuel_type = self.cleaned_data['fuel_type'],
            color = self.cleaned_data['color'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            price = self.cleaned_data['price'],
            state = self.cleaned_data['state'],
            photo = self.cleaned_data['photo'],
        )
        car.save()  
        return car
    
class CarModelForm(forms.ModelForm):
        class Meta:
             model = Car
             fields = '__all__'