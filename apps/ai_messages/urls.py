from django.urls import path
from . import views

app_name = 'messages'

urlpatterns = [
    path('/<int:id>', views.message, name='message'),
]