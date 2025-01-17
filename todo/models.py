from django.db import models

# Create your models here.

class Task(models.Model):
    tname=models.CharField(max_length=100)
    tdesc=models.CharField(max_length=5000)
    completed = models.BooleanField(default=False)