from datetime import datetime, timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(
        max_length=150, verbose_name="First name", default="Aquarium"
    )
    last_name = models.CharField(
        max_length=150, verbose_name="Last name", null=True, blank=True
    )
    streak_count = models.IntegerField(default=0, verbose_name="Streak count")
    settings = models.JSONField(default=dict, verbose_name="Settings")
    in_leaderboard = models.BooleanField(
        default=True, verbose_name="In leaderboard", db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name"]

    def __str__(self):
        return self.email

    def update_streak(self):
        events = (
            self.events.filter(in_streak=True)
            .order_by("-date")
            .values_list("date", flat=True)
        )
        if not events:
            self.streak_count = 0
            self.save()
            return 0

        today = datetime.today().date()
        if events[0] < today - timedelta(days=1):
            self.streak_count = 0
            self.save()
            return 0

        streak = 1
        prev = events[0]
        for current in events[1:]:
            diff = (prev - current).days
            if diff == 1:
                streak += 1
                prev = current
            elif diff == 0:
                continue
            else:
                break

        self.streak_count = streak
        self.save()
        return streak
