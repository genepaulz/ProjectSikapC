from django import forms
from .models import Rating

class ratingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = [
            'raterEmail',
            'rating',
            'numOfRates'
        ]
