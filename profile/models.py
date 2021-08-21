from django.db import models
from django.utils import timezone

class message(models.Model):
    name = models.CharField(max_length = 250)
    subject = models.CharField(max_length = 250)
    email = models.EmailField()
    message_recieved = models.TextField()
    date_recieved = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name
