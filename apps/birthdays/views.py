from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.birthdays.models import Birthday
from .forms import BirthdayForm

def home(request):
    birthdays = Birthday.objects.all()
    
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
            return redirect('birthdays:add')  # change this to your actual view
    else:
        form = BirthdayForm()
    return render(request, 'birthdays/add_birthday.html', {'form': form})