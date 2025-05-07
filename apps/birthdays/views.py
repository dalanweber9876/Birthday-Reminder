from django.shortcuts import render
from django.http import HttpResponse
from apps.birthdays.models import Birthday

def home(request):
    birthdays = Birthday.objects.all()
    
    return render(request, 'birthdays/home.html', {
        'birthdays': birthdays
        })


def add_birthday(request):
    return render(request, 'birthdays/add_birthday.html')