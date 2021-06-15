from django import forms


class userForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'firstname',
            'lastname',
            'industry',
            'region',
            'province',
            'city',
            'isVerified',
            'isDeleted',
            'user_type'
        ]

class applicantForm(forms.ModelForm):

    class Meta:
        model = Applicant
        fields = [
            'applicantUser',
            'age',
            'position',
            'ratings'
        ]

class employerForm(forms.ModelForm):

    class Meta:
        model = Employer
        field = [
            'employerUser',
            'companyName',
            'matches'
        ]
