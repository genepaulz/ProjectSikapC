from django import forms
from .models import *

class postsForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = [
            'email',
            'firstname',
            'lastname',
            'industry',
            'region',
            'province',
            'city',
            'age',
            'industry',
            'yearsOfExperience',
            'position',
            'dateAdded',
            'isAgeViewable',
            'isDeleted'
        ]