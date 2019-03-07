from django.db import models
from core.models.model_abstract import TimestampedModel


class Profile(TimestampedModel):
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True)
    image = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
