from django.core.mail import send_mail
from django.conf import settings
from pytz import timezone as pytz_timezone
from django.utils import timezone

def send_birthday_reminder_email(user):

    birthdays = user.birthdays.all()
    now_utc = timezone.now()
    user_tz = pytz_timezone(user.userprofile.timezone)
    now_local_date = now_utc.astimezone(user_tz).date()
    names = []

    for birthday in birthdays:

        if birthday.date.month == now_local_date.month and birthday.date.day == now_local_date.day:
            names.append(birthday.name)


    print(names)
    if names:
        subject = "It's time to party!"

        formatted_names = format_names(names)
        message = f"Today is {formatted_names}'s birthday! Go to the Birthday Reminder website to get some help writing a message to send them!"
    
        from_email = f"Birthday Reminder <{settings.EMAIL_HOST_USER}>"
        recipient_list = [user.email]
        print(user.email)

        send_mail(subject, message, from_email, recipient_list)

def format_names(names):
    if len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f"{names[0]} and {names[1]}"
    else:
        return ", ".join(names[:-1]) + f", and {names[-1]}"