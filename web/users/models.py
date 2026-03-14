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
    settings = models.JSONField(default=dict, verbose_name="Settings")
    streak_count = models.IntegerField(default=0, verbose_name="Streak count")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    events_last_updated_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Events last updated at"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name"]

    def __str__(self):
        return self.email
