from email.policy import default
from turtle import title
from django.db import models
import uuid

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField()