from django import forms
from .models import Posts

class postsForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = [
            'email',
            'firstname',
            'lastname',
            'region',
            'province',
            'city',
            'age',
            'industry',            
            'yearsOfExperience',
            'position',
            'dateAdded',
            'isAgeViewable',
            'isDeleted',
            # 'applicantID'
        ]