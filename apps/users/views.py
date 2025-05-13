from django.shortcuts import render, redirect
from .forms import UserCreationForm


def account(request):
    if request.user.is_authenticated:
        print("User is logged in:", request.user.username)
        return render(request, 'users/account.html', {
        'isAuthenticated': True
        })
    else:
        print("User is not logged in.")
        return redirect('users:login')
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})
