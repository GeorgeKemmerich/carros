from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
        class Meta:
             model = Car
             fields = '__all__'

        def clean_price(self):
               price = self.cleaned_data.get('price') 
               if price < 8000:
                self.add_error('price', 'Valor Mínimo R$8,000!')
                return price