from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def profile_view(request):
    return render(request, 'userapp/profile.html')

def resiter_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    form = RegistrationForm()
    return render(request, "userapp/registerForm.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("foods")
    
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    form = LoginForm()
    return render(request, 'userapp/loginForm.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')