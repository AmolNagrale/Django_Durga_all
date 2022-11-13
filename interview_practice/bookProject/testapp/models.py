from django.db import models

# Create your models here.

class Book(models.Model):
    ename=models.CharField(max_length=64)
    location=models.CharField(max_length=64)
    salary=models.IntegerField()
    qualification=models.CharField(max_length=64)
