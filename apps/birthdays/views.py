from django.shortcuts import render, redirect
from django.db.models.functions import ExtractMonth, ExtractDay
from django.utils.timezone import now
from django.http import HttpResponse
from apps.birthdays.models import Birthday
from .forms import BirthdayForm

def days_until_birthday(bday):
    today = now().date()

    this_year_birthday = bday.date.replace(year=today.year)
    if this_year_birthday < today:
        this_year_birthday = bday.date.replace(year=today.year + 1)
    return (this_year_birthday - today).days

def home(request):
    birthdays = sorted(Birthday.objects.all(), key=days_until_birthday)
    
    return render(request, 'birthdays/home.html', {
        'birthdays': birthdays
        })


# def add_birthday(request):
#     return render(request, 'birthdays/add_birthday.html')

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