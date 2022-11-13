from django.db import models
from django.db.models.base import Model

# Create your models here.
class Customer(models.Model):
    ename=models.CharField(max_length=64)
    eno=models.IntegerField()
    mailid=models.CharField(max_length=64)
    phonenumber=models.IntegerField()
    age=models.IntegerField()