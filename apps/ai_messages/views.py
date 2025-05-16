from django.shortcuts import render
from apps.birthdays.models import Birthday
from .utils import generate_birthday_message

def message(request, id):
    birthday = Birthday.objects.get(id = id)
    message = None

    if request.method == "POST":
        tone = request.POST.get("tone", "short and sweet")
        message = generate_birthday_message(birthday, tone)

    return render(request, 'ai_messages/message.html', {
        "birthday": birthday,
        "message": message
    })

# def generate_message(request):

#     message = generate_birthday_message(birthday)
#     print(message)

#     return render(request, 'ai_messages/message.html')