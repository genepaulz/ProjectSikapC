from django import forms

class postsForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = [
            'email',
            'firstname',
            'surname',
            'position',
            'yearsOfExperience',
            'industry',
            'region',
            'province',
            'city',
            'age',
            'dateadded',
            'isAgeViewable'
        ]