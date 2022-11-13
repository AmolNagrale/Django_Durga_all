from django.db import models
from django.urls import reverse

# Create your models here.
class Beer(models.Model):
    name=models.CharField(max_length=128)
    taste=models.CharField(max_length=128)
    color=models.CharField(max_length=128)
    price=models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
        