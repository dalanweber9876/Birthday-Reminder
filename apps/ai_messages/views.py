from django.shortcuts import render
from apps.birthdays.models import Birthday
from .utils import generate_birthday_message

def message(request, id):
    birthday = Birthday.objects.get(id = id)

    message = generate_birthday_message(birthday)
    print(message)

    return render(request, 'ai_messages/message.html')