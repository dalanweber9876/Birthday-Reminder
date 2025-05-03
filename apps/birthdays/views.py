from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    birthdays = [
        {'name': 'Alice', 'date': '2023-01-01'},
        {'name': 'Bob', 'date': '2023-02-02'},
        {'name': 'Charlie', 'date': '2023-03-03'},
    ]
    return render(request, 'birthdays/home.html', {
        'birthdays': birthdays
        })


def add_birthday(request):
    return render(request, 'birthdays/add_birthday.html')