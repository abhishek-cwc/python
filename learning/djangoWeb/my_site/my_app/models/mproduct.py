from django.db import models
from . import mcategory

class mproduct(models.Model):
    name = models.CharField(max_length=25)
    sku = models.CharField(max_length=25)
    price = models.FloatField()
    qty = models.IntegerField()
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(mcategory, on_delete=models.CASCADE, null=True, blank=True)


    @staticmethod
    def getAllProducts():
        return mproduct.objects.all()
