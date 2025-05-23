from django.db import models

class mcustomer(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=400)

    @staticmethod
    def create(data):
        try:
            mcustomer.objects.create(name=data['name'], email=data['email'], password=data['password'])
            return True
        except Exception as e:
            raise ValueError(str(e))
    