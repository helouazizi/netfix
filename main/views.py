from django.shortcuts import render , redirect
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request,'main/home.html')



def logout_user(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to login page after logout