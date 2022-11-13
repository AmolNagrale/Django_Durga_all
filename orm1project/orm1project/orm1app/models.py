from django.db import models
from django.db.models.base import Model

# Create your models here.
class Employee1(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=128)
    
    