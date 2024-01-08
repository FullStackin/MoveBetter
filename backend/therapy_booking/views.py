from django.shortcuts import render
from rest_framework import viewsets
from .models import Therapy, Booking
from .serializers import TherapySerializer, BookingSerializer

class TherapyViewSet(viewsets.ModelViewSet):
    queryset = Therapy.objects.all()
    serializer_class = TherapySerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
