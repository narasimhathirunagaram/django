# pricing/models.py
from django.db import models

class PricingConfig(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]
    day_of_week = models.CharField(max_length=3, choices=DAY_CHOICES)
    dbp = models.DecimalField(max_digits=8, decimal_places=2, default=80.0)
    
    def __str__(self):
        return f"{self.get_day_of_week_display()} - DBP: {self.dbp}"
