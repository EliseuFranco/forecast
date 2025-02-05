from django import forms


class ForecastForm(forms.Form):
    city = forms.CharField(max_length=50, required=True,widget=forms.TextInput(attrs={
        'placeholder':'Enter the city name',
        'autocomplete':'off'
    }))