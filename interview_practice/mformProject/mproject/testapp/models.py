from django.db import models

# Create your models here.
class Student(models.Model):
    ename=models.CharField(max_length=30)
    marks=models.IntegerField()

    
    