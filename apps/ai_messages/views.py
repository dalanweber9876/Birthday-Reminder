from django.shortcuts import render
from apps.birthdays.models import Birthday
from .utils import *
from .generator import *

def message_openai(request, id):
    birthday = Birthday.objects.get(id = id)
    message = None

    if request.method == "POST":
        tone = request.POST.get("tone", "short and sweet")
        message = generate_message_openai(birthday, tone)

    return render(request, 'ai_messages/message.html', {
        "birthday": birthday,
        "message": message
    })

def message_custom(request, id):
    birthday = Birthday.objects.get(id = id)
    message = None

    if request.method == "POST":
        name = birthday.name
        background = birthday.background
        message = generate_message_custom(name, background)

    return render(request, "ai_messages/message_custom.html", {"message": message})