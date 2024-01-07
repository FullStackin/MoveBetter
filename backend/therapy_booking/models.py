# Import necessary Django modules
from django.db import models
from django.contrib.auth.models import AbstractUser, User

# -------------------------------------------------------------------
# Custom User Model (Optional)
# -------------------------------------------------------------------
# Extend the default User model to include a phone_number field
class CustomUser(AbstractUser):

    # Additional field for phone number
    phone_number = models.CharField(max_length=15, blank=True)

    # String representation for displaying the user
    def __str__(self):
        return self.username

# -------------------------------------------------------------------
# Therapy Model
# -------------------------------------------------------------------
# Model for storing information about different therapies
class Therapy(models.Model):

    # Fields for therapy details
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in minutes")
    image = models.ImageField(upload_to='therapy_images/', blank=True, null=True)
    availability = models.BooleanField(default=True)

    # String representation for displaying the therapy
    def __str__(self):
        return self.name

# -------------------------------------------------------------------
# Booking Model
# -------------------------------------------------------------------
# Model for managing therapy appointments
class Booking(models.Model):

    # Define available booking statuses
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    # Fields for booking details
    therapy = models.ForeignKey(Therapy, on_delete=models.CASCADE)  # Link to the booked therapy
    client_name = models.CharField(max_length=100)
    client_contact = models.CharField(max_length=100)
    date = models.DateTimeField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    payment_status = models.BooleanField(default=False)

    # String representation for displaying the booking
    def __str__(self):
        return f"{self.therapy.name} booking for {self.client_name}"

# -------------------------------------------------------------------
# Review Model
# -------------------------------------------------------------------
# Model for storing user reviews about therapies
class Review(models.Model):

    # Fields for review details
    therapy = models.ForeignKey(Therapy, on_delete=models.CASCADE)  # Link to the reviewed therapy
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who wrote the review
    rating = models.IntegerField()
    comment = models.TextField(blank=True)

    # String representation for displaying the review
    def __str__(self):
        return f"Review by {self.user.username} for {self.therapy.name}"

# -------------------------------------------------------------------
# Appointment Slot Model (Optional)
# -------------------------------------------------------------------
# Model for managing specific time slots for appointments (optional feature)
class AppointmentSlot(models.Model):

    # Fields for appointment slot details
    therapy = models.ForeignKey(Therapy, on_delete=models.CASCADE)  # Link to the therapy for which the slot is available
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)

    # String representation for displaying the appointment slot
    def __str__(self):
        return f"{self.therapy.name} slot on {self.start_time}"
