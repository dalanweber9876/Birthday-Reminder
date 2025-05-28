from django.urls import path
from . import views

app_name = 'messages'

urlpatterns = [
    path('<int:id>/', views.message_custom, name='message'),
    # path('generate_message/', views.generate_message, name='generate_message'),
]