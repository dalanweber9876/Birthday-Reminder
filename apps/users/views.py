from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserEditForm
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from apps.birthdays.models import User
from django.contrib import messages
import json
import pytz



def account(request):
    if request.user.is_authenticated:
        return render(request, 'users/account.html', {
            "user": request.user,
        })
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

def edit_account(request, id):
    user =  User.objects.get(id = id)

    if request.user != user:
        return redirect('users:account')

    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=user) 
        if form.is_valid():
            form.save()
            messages.success(request, "Account edited successfully!")
            return redirect('users:account')
    
    else:
        form = CustomUserEditForm(instance=user)

    return render(request, 'users/edit_account.html', {
        'form': form
    })