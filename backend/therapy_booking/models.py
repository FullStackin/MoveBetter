from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Extend the default User model (optional)
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username

# Model for different therapies
class Therapy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in minutes")
    image = models.ImageField(upload_to='therapy_images/', blank=True, null=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Model for booking appointments
class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    therapy = models.ForeignKey(Therapy, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_contact = models.CharField(max_length=100)
    date = models.DateTimeField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.therapy.name} booking for {self.client_name}"

# Model for reviews or feedback
class Review(models.Model):
    therapy = models.ForeignKey(Therapy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.therapy.name}"

# Model for appointment slots (optional)
class AppointmentSlot(models.Model):
    therapy = models.ForeignKey(Therapy, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.therapy.name} slot on {self.start_time}"
