from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('profile/', views.account, name='account'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='users:login'), name='logout'),
    path('register/', views.register, name='register'),
    path('set_timezone/', views.set_timezone, name='set_timezone'),
    path('edit/<int:id>', views.edit_account, name='edit'),
]
