from django.shortcuts import render , redirect
from django.contrib.auth import logout
from users.models import CompanyProfile
from services.models import Service

# Create your views here.
def home(request):
    # def home(request):
    service = request.GET.get('service')
    services = Service.objects.all()
    if service:
        services = services.filter(field=service)
    return render(request, 'main/home.html', {'services': services, 'selected_service': service,'serv_title':service})

    # return render(request,'main/home.html')



def logout_user(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to login page after logout