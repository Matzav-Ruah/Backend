from django.db import models
from django.conf import settings

EMOTIONAL_STATES = [
    ("bad", "Bad"),
    ("neutral", "Neutral"),
    ("good", "Good"),
]


class Event(models.Model):
    emotional_state = models.CharField(
        max_length=10, choices=EMOTIONAL_STATES, verbose_name="Emotional state"
    )
    event_data = models.JSONField(verbose_name="Event data")
    date = models.DateField(verbose_name="Date")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="User",
        related_name="events",
    )

    def __str__(self):
        return self.emotional_state
