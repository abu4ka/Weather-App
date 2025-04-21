from django import forms

class CityForm(forms.Form):
    city = forms.CharField(
        label='Город или страна',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400',
            'placeholder': 'Например, Tashkent'
        })
    )


