from django.db import models

# Create your models here.

class customer(models.Model):
    fname = models.CharField(max_length=20)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=200)
