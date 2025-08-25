# learn/models.py
from django.db import models

# Create your models here.


class learn(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
