from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # Include the URLs for the home page (birthdays app)
    path('', include('apps.birthdays.urls', namespace='birthdays')),

    # Include the URLs for the user account page (users app)
    path('accounts/', include('apps.users.urls', namespace='users')),

    # Include the URLs for the messaging page (ai_messages app)
    path('message/', include('apps.ai_messages.urls', namespace='messages')),
]
