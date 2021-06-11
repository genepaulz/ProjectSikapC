from dango import forms
from .models import *

class ratingForm(forms.ModelForm):

    class Meta:
        model = Rating
        field = [
            'raterEmail',
            'rating',
            'numOfRates'
        ]
