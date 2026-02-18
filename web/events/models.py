from django.db import models

EMOTIONAL_STATES = [
    ("bad", "Bad"),
    ("neutral", "Neutral"),
    ("good", "Good"),
]


class Event(models.Model):
    emotional_state = models.CharField(
        max_length=10, choices=EMOTIONAL_STATES, verbose_name="Emotional state"
    )
    data = models.JSONField(verbose_name="Data")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return self.emotional_state
