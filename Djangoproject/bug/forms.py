from django import forms
from .models import Bug
from django.utils import timezone
from django.forms.widgets import DateInput

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['description', 'bug_type', 'report_date', 'status']

        widgets = {
        'report_date': forms.DateInput(attrs={'type': 'date'}),
        }
