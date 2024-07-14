from django.shortcuts import render, redirect
from .forms import ServiceRequestForm

def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_request_success')
    else:
        form = ServiceRequestForm()
    return render(request, 'create_service_request.html', {'form': form})

def service_request_success(request):
    return render(request, 'service_request_success.html')