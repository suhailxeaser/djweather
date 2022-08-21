from django import forms

class CityWeatherForm(forms.Form):
    city_name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city_name'].widget.attrs.update({'class' : 'input', 'placeholder' : 'City Name'})     
