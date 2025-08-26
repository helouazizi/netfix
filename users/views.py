# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import CompanyRegistrationForm, CustomerRegistrationForm, EmailAuthenticationForm


def register(request):
    return render(request, 'users/register.html')


def register_company(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Company account created successfully!')
            return redirect('login')
      
    else:
        form = CompanyRegistrationForm()
        

    return render(request, 'users/register_company.html', {'form': form})



def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerRegistrationForm()

    return render(request, 'users/register_customer.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')
    else:
        form = EmailAuthenticationForm()

    return render(request, 'users/login.html', {'form': form})
