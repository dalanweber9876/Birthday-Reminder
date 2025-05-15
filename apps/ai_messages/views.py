from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser
from apps.birthdays.models import Birthday

def message(request):
    return render(request, 'ai_messages/message.html')