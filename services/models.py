# services/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone

User = get_user_model()

class Service(models.Model):
    FIELD_CHOICES = [
        ('Air Conditioner', 'Air Conditioner'),
        ('All in One', 'All in One'),
        ('Carpentry', 'Carpentry'),
        ('Electricity', 'Electricity'),
        ('Gardening', 'Gardening'),
        ('Home Machines', 'Home Machines'),
        ('Housekeeping', 'Housekeeping'),
        ('Interior Design', 'Interior Design'),
        ('Locks', 'Locks'),
        ('Painting', 'Painting'),
        ('Plumbing', 'Plumbing'),
        ('Water Heaters', 'Water Heaters'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    field = models.CharField(max_length=50, choices=FIELD_CHOICES)
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    hours = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} requested {self.service.name}"