"""
URL configuration for birthday_reminder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # Include the URLs for the home page (birthdays app)
    path('', include('apps.birthdays.urls', namespace='birthdays')),

    # Include the URLs for the user account page (users app)
    path('account', include('apps.users.urls', namespace='users')),
]
