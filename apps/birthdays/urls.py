from django.urls import path
from . import views

app_name = 'birthdays'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_birthday, name='add'),
]