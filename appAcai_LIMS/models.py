from django.db import models

# Create your models here.

class Library(models.Model):
    Publisher=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    Title=models.CharField(max_length=100)
    PageCount=models.IntegerField()
    Category=models.CharField(max_length=100)
    ShelfLocation=models.CharField(max_length=100)
    PublishedDate=models.DateField()
    IsInstock=models.BooleanField()
    DateCheckedOut=models.DateField()
