from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')

def login_redirect(request):
    return redirect('social:begin', backend='github')

@login_required
def dashboard(request):
    # Placeholder for now, we'll add GitHub data fetching here next
    username = request.user.username
    return render(request, 'dashboard.html', {'username': username})

def logout_view(request):
    logout(request)
    return redirect('home')
