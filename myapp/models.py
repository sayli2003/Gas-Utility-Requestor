from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add custom fields here if needed
    pass



class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]
    Request_CHOICES = [
        ('Service Installation', 'Service Installation'),
        ('Service Connection', 'Service Connection'),
        ('Service Disconnection', 'Service Disconnection'),
        ('Service Inspection', 'Service Inspection'),
        ('Meter Reading', 'Meter Reading'),
        ('Billing Inquiry', 'Billing Inquiry'),
        ('Emergency Service', 'Emergency Service'),
        ('Maintenance', 'Maintenance'),
        ('General Inquiry', 'General Inquiry'),

    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    service_type = models.CharField(max_length=100, choices=Request_CHOICES, default='General Inquiry')
    description = models.TextField()
    upload = models.FileField(upload_to='documents/', blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_type
