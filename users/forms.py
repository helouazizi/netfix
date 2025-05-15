from django import forms
from django.contrib.auth import authenticate
from .models import CostumUser, Customerprofile , CompanyProfile


# -----------------------
# Customer Registration Form
# -----------------------

class CustomerRegistrationForm(forms.ModelForm):
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
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_customer = True  # Set the flag for the customer user
        if commit:
            user.save()

            # Create related profile
            Customerprofile.objects.create(
                user=user,
                date_of_birth=self.cleaned_data['date_of_birth']
            )

        return user


# -----------------------
# Company Registration Form
# -----------------------

class CompanyRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    field_of_work = forms.ChoiceField(choices=CompanyProfile.FIELD_OF_WORK_CHOICES)

    class Meta:
        model = CostumUser
        fields = ['email', 'username', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        
        # Check if passwords match
        if cleaned_data.get("password") != cleaned_data.get("password_confirm"):
            self.add_error('password_confirm', "Passwords do not match.")
        
        return cleaned_data

    def save(self, commit=True):
        # Save the user first
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_company = True  # Set the flag for the company user
        print("DEBUG: is_company before save =", user.is_company)  # Debug line
        if commit:
            user.save()

        # Create the CompanyProfile with the field_of_work data
        company_profile = CompanyProfile(
            user=user,
            field_of_work=self.cleaned_data['field_of_work']
        )
        company_profile.save()

        return user
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
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("")
            self.user = user
        return cleaned_data

    def get_user(self):
        return getattr(self, 'user', None)

