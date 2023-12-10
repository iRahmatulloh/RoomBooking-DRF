from django.db import models
from django.utils import timezone


# Create your models here.
class FacebookRoom(models.Model):
    room_number = models.IntegerField(unique=True)
    is_booked = models.BooleanField(default=False)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Room {self.room_number}"


class GoogleRoom(models.Model):
    room_number = models.IntegerField(unique=True)
    is_booked = models.BooleanField(default=False)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Room {self.room_number}"