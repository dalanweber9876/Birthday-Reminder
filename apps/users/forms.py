from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import pytz

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    timezone = forms.ChoiceField(
        choices=[(tz, tz) for tz in pytz.all_timezones],
        required=True,
        label="Timezone"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'timezone']
