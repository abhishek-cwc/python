from django.db import models

class address(models.Model):
    COUNTRY_CHOICES = [
        ('IN', 'India'),
        ('US', 'United States'),
        ('UK', 'United Kingdom'),
    ]
    city = models.CharField(max_length=20)
    state = models.CharField(max_length= 20)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='IN')
