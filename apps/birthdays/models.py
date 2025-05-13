from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Birthday(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='birthdays')
    name = models.CharField(max_length=100)
    date = models.DateField()
    relationship = models.CharField(max_length=100)
    background = models.TextField(blank=True)  # Optional
    email = models.EmailField(blank=True, null=True)  # Optional
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional

    def days_until_birthday(self):
        today = now().date()

        # Update the birthday date to this year
        birthday = self.date.replace(year=today.year)

        # If the birthday has already passed this year, set it to next year
        # (dates that have already happened are less than today's date when compared).
        if birthday < today:
            birthday = self.date.replace(year=today.year + 1)
        return (birthday - today).days

    def __str__(self):
        return self.name