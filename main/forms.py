from django import forms

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