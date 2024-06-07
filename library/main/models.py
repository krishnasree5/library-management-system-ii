from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    TYPE_CHOICES = [
        ('Student', 'student'),
        ('Staff', 'staff')
    ]
    type_is = models.CharField(max_length=10, choices=TYPE_CHOICES,default='student')

    def __str__(self):
        return self.username
