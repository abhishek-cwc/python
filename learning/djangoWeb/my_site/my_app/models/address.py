from django.db import models
from . import customer

class address(models.Model):
    COUNTRY_CHOICES = [
        ('IN', 'India'),
        ('US', 'United States'),
        ('UK', 'United Kingdom'),
    ]
    city = models.CharField(max_length=20)
    state = models.CharField(max_length= 20)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='IN')
    customer = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='addresses', null=True, blank=True)
