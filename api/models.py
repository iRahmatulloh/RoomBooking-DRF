from django.db import models


# Create your models here.
class Room(models.Model):
    room_number = models.IntegerField(unique=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Room {self.room_number}"
