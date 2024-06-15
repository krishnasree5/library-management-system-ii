from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    TYPE_CHOICES = [
        ('Non-staff', 'non-staff'),
        ('Staff', 'staff')
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES,default='non-staff')

    def __str__(self):
        return self.username
