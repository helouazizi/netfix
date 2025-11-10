
from django.shortcuts import render , redirect
from django.contrib.auth import logout
from django.db.models import Count
# from users.models import CompanyProfile
from services.models import Service

# Create your views here.
def main(request):
    # def home(request):
    service = request.GET.get('service')
    services = Service.objects.all()
    if service:
        services = services.filter(field=service)
   
    # for serv in services :
    #     print(serv.de)
        
    # Annotate serv.ices with request count and order by most requested
    most_requested_services = services.annotate(
        num_requests=Count('servicerequest')
    ).order_by('-num_requests')[:5]  # Top 5 most requested services
    return render(request, 'main/index.html', {'services': most_requested_services, 'selected_service': service,'serv_title':service})



def logout_user(request):
    logout(request)  # Log the user out
    return redirect('main')  # Redirect to login page after logout




# main/views.py
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

def custom_403(request, exception):
    return render(request, '403.html', status=403)

def custom_400(request, exception):
    return render(request, '400.html', status=400)
