# auth/models.py
from django.db import models

# Create your models here.



class auth(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__ (self):
        return self.name