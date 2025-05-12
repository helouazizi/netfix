from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # If the user is valid, log them in
            auth_login(request, user)
            messages.success(request, 'You have logged in successfully!')
            return redirect('home')  # Redirect to a page after successful login
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'users/login.html')


def register(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Your account has been created successfully!')
    #         return redirect('login')  # Redirect to login page after successful registration
    #     else:
    #         messages.error(request, 'Please correct the error below.')
    # else:
    #     form = UserCreationForm()
    
    return render(request, 'users/register.html')