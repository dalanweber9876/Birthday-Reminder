from django.urls import path
from . import views

app_name = 'birthdays'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_birthday, name='add'),
    path('view/<int:id>/', views.view_birthday, name='view'),
    path('edit/<int:id>/', views.edit_birthday, name='edit'),
    path('delete/<int:id>/', views.delete_birthday, name='delete'),
]