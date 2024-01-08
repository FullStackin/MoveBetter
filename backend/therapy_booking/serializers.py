from rest_framework import serializers
from .models import Therapy, Booking


class TherapySerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapy
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
