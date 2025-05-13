from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import CostumUser, Customerprofile , CompanyProfile


# -----------------------
# Customer Registration Form
# -----------------------

class  CustomerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CostumUser
        fields = ['email', 'username', 'password', 'password_confirm', 'date_of_birth']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("password_confirm"):
            self.add_error('password_confirm', "Passwords do not match.")
        return cleaned_data



# -----------------------
# Company Registration Form
# -----------------------
class CompanyRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    field_of_work = forms.CharField()

    class Meta:
        model = CostumUser
        fields = ['email', 'username', 'password', 'password_confirm', 'field_of_work']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("password_confirm"):
            self.add_error('password_confirm', "Passwords do not match.")
        return cleaned_data
    
    
# -----------------------
# Login Form
# -----------------------
class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise ValidationError("Invalid email or password")
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user