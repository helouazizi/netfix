from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import CompanyRegistrationForm, CustomerRegistrationForm, EmailAuthenticationForm
from .models import CompanyProfile, Customerprofile, CostumUser




def register(request):
    return render(request, 'users/register.html')



# -----------------------
# Company Registration View
# -----------------------
def register_company(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            # Create base user
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            field_of_work = form.cleaned_data['field_of_work']

            user = CostumUser.objects.create_user(email=email, username=username, password=password)
            CompanyProfile.objects.create(user=user, field_of_work=field_of_work)

            messages.success(request, 'Company account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CompanyRegistrationForm()

    return render(request, 'users/register_company.html', {'form': form})

# -----------------------
# Customer Registration View
# -----------------------
def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            date_of_birth = form.cleaned_data['date_of_birth']

            user = CostumUser.objects.create_user(email=email, username=username, password=password)
            Customerprofile.objects.create(user=user, date_of_birth=date_of_birth)

            messages.success(request, 'Customer account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerRegistrationForm()

    return render(request, 'users/register_customer.html', {'form': form})

# -----------------------
# Login View
# -----------------------
def login(request):
     if request.method == 'POST':
        form = EmailAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')  # Change to your actual homepage route name
        else:
            messages.error(request, 'Invalid login credentials.')
     else:
         form = EmailAuthenticationForm()

         return render(request, 'users/login.html', {'form': form})