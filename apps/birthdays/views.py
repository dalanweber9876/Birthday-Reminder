from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser
from apps.birthdays.models import Birthday
from .forms import BirthdayForm

def home(request):
    if isinstance(request.user, AnonymousUser):
        return render(request, 'birthdays/home_no_account.html')

    birthdays = sorted(Birthday.objects.filter(user = request.user), key=lambda b: b.days_until_birthday())
    return render(request, 'birthdays/home.html', {
        'birthdays': birthdays,
        'user': request.user,
        })

def add_birthday(request):
    if request.method == 'POST':
        form = BirthdayForm(request.POST)
        if form.is_valid():
            birthday = form.save(commit=False)
            birthday.user = request.user
            birthday.save()
            return redirect('birthdays:add')
    else:
        form = BirthdayForm()
    return render(request, 'birthdays/add_birthday.html', {'form': form})