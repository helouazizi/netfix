from django.shortcuts import render , redirect
from django.contrib.auth import logout
from users.models import CompanyProfile

# Create your views here.
def home(request):
    # def home(request):
    service = request.GET.get('service')
    companies = CompanyProfile.objects.all()
    if service:
        companies = companies.filter(field_of_work=service)
    return render(request, 'main/home.html', {'companies': companies, 'selected_service': service})

    # return render(request,'main/home.html')



def logout_user(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to login page after logout