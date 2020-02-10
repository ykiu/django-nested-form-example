from django.db import models

# Create your models here.

class Auther(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    auther = models.ForeignKey(to=Auther, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
