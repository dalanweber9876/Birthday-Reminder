from django import forms
from .models import Birthday

class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = ['name', 'date', 'relationship', 'background', 'email', 'phone_number']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'background': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'name': 'Name',
            'date': 'Birthday Date',
            'relationship': 'Relationship',
            'background': 'Background/Notes',
            'email': 'Email (optional)',
            'phone_number': 'Phone Number (optional)',
        }
