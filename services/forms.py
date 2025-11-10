# services/forms.py
from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['created_at', 'company']