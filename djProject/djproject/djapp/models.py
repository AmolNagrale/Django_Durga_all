from django.db import models

# Create your models here.
class Hydjobs(models.Model):
    date= models.DateField()
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField()
    phonenumber = models.IntegerField()

class Chnjobs(models.Model):
    date= models.DateField()
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField()
    phonenumber = models.IntegerField()

class Punejobs(models.Model):
    date= models.DateField()
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField()
    phonenumber = models.IntegerField()

class Banjobs(models.Model):
    date= models.DateField()
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField()
    phonenumber = models.IntegerField()
