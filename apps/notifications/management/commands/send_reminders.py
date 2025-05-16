from django.core.management.base import BaseCommand
from apps.users.models import UserProfile
from apps.notifications.utils import send_birthday_reminder_email
from pytz import timezone as pytz_timezone
from django.utils import timezone

class Command(BaseCommand):
    help = "Send birthday reminders at 6 AM local time"

    def handle(self, *args, **kwargs):
        now_utc = timezone.now()

        for profile in UserProfile.objects.select_related("user"):
            print(f"for loop: {profile}")
            if profile.timezone:
                print(f"if statement {profile}")
                try:
                    user_tz = pytz_timezone(profile.timezone)
                    local_time = now_utc.astimezone(user_tz).time()
                    print("Step 1")

                    # Send the message at 6am local time. Change the number for testing.
                    if local_time.hour == 23: 
                        print("Step 2")
                        send_birthday_reminder_email(profile.user)
                except Exception as e:
                    self.stderr.write(f"Error with {profile.user.username}: {e}")