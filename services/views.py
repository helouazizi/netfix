
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm
from .models import Service ,ServiceRequest




def servives(request):
    services = Service.objects.select_related('company').all()
    return  render(request,'services/services.html',{'services':services})


@login_required
def create_service(request):
    if not request.user.is_authenticated or not request.user.is_company:
        return redirect('services')  # or return a 403

    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.company = request.user
            service.save()
            return redirect('services')  # Redirect to services page or detail
    else:
        form = ServiceForm()

    return render(request, 'services/create_service.html', {'form': form})

@login_required
def profile_view(request):
    user = request.user

    if user.is_company:
        services = Service.objects.filter(company=user)
        return render(request, 'services/profile.html', {
            'user': user,
            'services': services,
            'is_company': True,
        })

    elif user.is_customer:
        requests = ServiceRequest.objects.filter(customer=user)
        return render(request, 'services/profile.html', {
            'user': user,
            'requests': requests,
            'is_customer': True,
        })

    # fallback in case neither
    return render(request, 'services/profile.html', {'user': user})

@login_required
def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'services/service_detail.html', {'service': service})



@login_required
def request_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == "POST" and request.user.is_customer:
        address = request.POST.get("address")
        hours = request.POST.get("hours")

        # You can add validations here

        ServiceRequest.objects.create(
            service=service,
            customer=request.user,
            address=address,
            hours=hours,
        )
        return redirect("profile")  # or to a success page

    return redirect("service_detail", service_id=service_id)