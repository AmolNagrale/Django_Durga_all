from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields import CharField

# Create your models here.

class ContactInfo1(models.Model):
    name=models.CharField(max_length=128)
    email=models.EmailField()
    address=models.CharField(max_length=256)
    class Meta:
        abstract=True

class Student1(ContactInfo1):
    rollno=models.IntegerField()
    mark=models.IntegerField()


class Teacher1(ContactInfo1):
    subject=models.CharField(max_length=128)
    salary=models.FloatField(max_length=128)

class Parent(models.Model):
    fd1=models.CharField(max_length=128)
    fd2=models.CharField(max_length=128)

class Child(Parent):
    fd3=models.CharField(max_length=128)
    fd4=models.CharField(max_length=128)

class Subchild(Child):
    fd5=models.CharField(max_length=128)
