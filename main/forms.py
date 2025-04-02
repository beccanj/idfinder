from django import forms
from django.contrib.auth.models import User

from main.models import Citizen, LostIDReport, RetrievalRequest

class CitizenForm(forms.ModelForm):
    class Meta:
        model = Citizen
        fields = ['first_name', 'last_name','national_id', 'phone_number', 'email']

class LostIDReportForm(forms.ModelForm):
    class Meta:
        model = LostIDReport
        fields = ['citizen', 'description', 'location']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 4})
        }

class RetrievalRequestForm(forms.ModelForm):
    class Meta:
        model = RetrievalRequest
        fields = ['report', 'citizen']

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data