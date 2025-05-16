# services/models.py
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# from django.utils import timezone

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
    # request_count = models.PositiveIntegerField(default=0)/
    # def clean(self):
        
    #     super().clean()

    #     # Prevent services from being "All in One"
    #     if self.field == "All in One":
    #         raise ValidationError("You cannot create a service with the 'All in One' field.")

    #     # If the company is not "All in One", they can only create services matching their own field
    #     if self.company.field != "All in One" and self.company.field != self.field:
    #         raise ValidationError(f"A {self.company.field} company can only create services in the same field.")


    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE,related_name='servicerequest')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    hours = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} requested {self.service.name}"