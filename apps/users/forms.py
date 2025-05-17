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


class CustomUserEditForm(forms.ModelForm):
    timezone = forms.ChoiceField(choices=[(tz, tz) for tz in pytz.all_timezones], required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        user = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if user:
            self.fields['timezone'].initial = user.userprofile.timezone

    def save(self, commit=True):
        user = super().save(commit)
        user.userprofile.timezone = self.cleaned_data['timezone']
        if commit:
            user.userprofile.save()
        return user
