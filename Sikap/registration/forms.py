from django import forms
from login.models import *

class userForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'firstname',
            'surname',
            'user_type',
            'isVerified',
            'companyName',
            'industry',
            'region',
            'province',
            'city',
            'age',
        ]