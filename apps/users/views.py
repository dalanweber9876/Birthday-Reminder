from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.management import call_command
import json
import pytz



def account(request):
    if request.user.is_authenticated:
        call_command('send_reminders')
        return render(request, 'users/account.html')
    else:
        return redirect('users:login')
    
def register(request):
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = user.userprofile
            profile.timezone = form.cleaned_data['timezone']
            profile.save()
            login(request, user)
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
            
            if tz in pytz.all_timezones:
                # Save to user profile or session
                profile = request.user.userprofile
                profile.timezone = tz
                profile.save()
                return JsonResponse({"status": "success"})
        return JsonResponse({"status": "error", "message": "Invalid timezone"}, status=400)
    return JsonResponse({"status": "error", "message": "Only POST allowed"}, status=405)