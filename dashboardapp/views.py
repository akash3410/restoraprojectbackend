from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
@login_required
def dashboard_view(request):
    if not request.user.is_superuser:
        return redirect('profile')
    return render(request, 'dashboardapp/dashboard.html')
