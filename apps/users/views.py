from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from apps.birthdays.models import Birthday
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json


def account(request):
    if request.user.is_authenticated:
        birthdays = sorted(Birthday.objects.filter(user = request.user), key=lambda b: b.days_until_birthday())
        return render(request, 'birthdays/home.html', {
        'isAuthenticated': True,
        'birthdays': birthdays,
        })
    else:
        print("User is not logged in.")
        return redirect('users:login')
    
def register(request):
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def set_timezone(request):
    if request.method == "POST":
        data = json.loads(request.body)
        tz = data.get("timezone")
        if tz:
            # Validate timezone string
            import pytz
            if tz in pytz.all_timezones:
                # Save to user profile or session
                profile = request.user.userprofile
                profile.timezone = tz
                profile.save()
                return JsonResponse({"status": "success"})
        return JsonResponse({"status": "error", "message": "Invalid timezone"}, status=400)
    return JsonResponse({"status": "error", "message": "Only POST allowed"}, status=405)