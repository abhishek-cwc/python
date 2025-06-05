# models.py
import uuid
from django.db import models
from . import customer  

class CustomerToken(models.Model):
    customer = models.OneToOneField(customer, on_delete=models.CASCADE)
    key = models.CharField(max_length=64, unique=True, default=uuid.uuid4)

    def __str__(self):
        return f"{self.customer.email} - {self.key}"
