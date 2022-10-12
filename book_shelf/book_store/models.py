from email.policy import default
from turtle import title
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    authors = models.CharField(max_lenght=100)
    is_bestselling = models.BooleanField()

    def __str__(self):
        return f"{self.title} ({self.rating})" #function to format string return from model