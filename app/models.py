from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GROCERY_2(models.Model):
    status_choices = [
        ('B', 'BOUGHT'),
        ('NA', 'NOT AVAILABLE'),
        ('P', 'PENDING'),
    ]
    name = models.CharField(max_length=122)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    status = models.CharField(max_length=3, choices=status_choices)
    date = models.DateField()
