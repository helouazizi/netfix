
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm
from .models import Service




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
