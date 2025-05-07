from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Birthday(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='birthdays')
    name = models.CharField(max_length=100)  # Name of the person
    date = models.DateField()  # Birthday date
    relationship = models.CharField(max_length=100)  # Relationship to the person (e.g., "Friend", "Family", etc.)
    background = models.TextField(blank=True)  # Background or notes about the person, optional
    email = models.EmailField(blank=True, null=True)  # Optional email field
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number field

    def __str__(self):
        return self.name