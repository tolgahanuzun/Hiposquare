import datetime

from django.db import models
from django.utils import timezone

class Square(models.Model):
    looking_for = models.CharField(max_length=200)
    locations = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.looking_for + ' - ' + self.locations

