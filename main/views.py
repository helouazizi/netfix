from django.shortcuts import render , redirect
from django.contrib.auth import logout
from django.db.models import Count
from users.models import CompanyProfile
from services.models import Service

# Create your views here.
def home(request):
    # def home(request):
    service = request.GET.get('service')
    services = Service.objects.all()
    if service:
        services = services.filter(field=service)
        
    # Annotate services with request count and order by most requested
    most_requested_services = services.annotate(
        num_requests=Count('servicerequest')
    ).order_by('-num_requests')[:5]  # Top 5 most requested services
    return render(request, 'main/home.html', {'services': most_requested_services, 'selected_service': service,'serv_title':service})




def logout_user(request):
    logout(request)  # Log the user out
    return redirect('home')  # Redirect to login page after logout