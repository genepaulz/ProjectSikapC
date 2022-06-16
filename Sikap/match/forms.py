from django import forms
#from match.models import Match

class matchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = [
            'employerID',
            'postsID',
            'applicantID',
        ]