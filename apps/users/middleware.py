from django.utils import timezone
import pytz

class UserTimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = None

        if request.user.is_authenticated:
            # assuming you have UserProfile and a timezone field
            tzname = getattr(request.user.userprofile, 'timezone', None)

        if not tzname:
            # fallback: you can get from session, or use default
            tzname = request.session.get('django_timezone')

        if tzname:
            try:
                timezone.activate(pytz.timezone(tzname))
            except Exception:
                timezone.deactivate()
        else:
            timezone.deactivate()  # fallback to default timezone

        response = self.get_response(request)
        return response
