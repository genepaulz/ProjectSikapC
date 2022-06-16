from django import forms
from .models import Match

class matchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = [
         
        ]