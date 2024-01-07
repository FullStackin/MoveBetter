from django.db import models

# Create your models here.

from django.db import models

class Therapy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Booking(models.Model):
    therapy = models.ForeignKey(Therapy, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    notes = models.TextField(blank=True)
