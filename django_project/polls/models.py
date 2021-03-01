from django.db import models
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    image_url=models.CharField(max_length=2000)

# Create your models here.
    def __str__(self):
        return self.name
class Person(models.Model):
    firstName=models.CharField(max_length=200)
    lasttName = models.CharField(max_length=200)
    email=models.EmailField()
class Student(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    batch=models.CharField(max_length=20)
    category=models.CharField(max_length=200)
    image_url=models.CharField(max_length=2000)
    created_date=models.DateTimeField(auto_now_add=True)