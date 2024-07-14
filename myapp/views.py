from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserSignupForm, UserLoginForm
from .forms import ServiceRequestForm

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {username}!')
            return redirect('/consumer/profile')  # Redirect to your dashboard view
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('login')

def profile(request):
    return render(request, 'dashboard.html')



def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('service_request_success')
        else:
            print(form.errors)
    else:
        form = ServiceRequestForm()
    return render(request, 'create_service_request.html', {'form': form})

def service_request_success(request):
    return render(request, 'service_request_success.html')