from email.policy import default
from turtle import title
from django.db import models
import uuid

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return f"book:{self.title}, rating:{self.rating}" #function to format string return from model