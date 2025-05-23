from django.db import models

class mcategory(models.Model):
    name = models.CharField(max_length=25)


    @staticmethod
    def getAllCategory():
        return mcategory.objects.all()
