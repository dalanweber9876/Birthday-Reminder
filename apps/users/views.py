from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from apps.birthdays.models import Birthday


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
